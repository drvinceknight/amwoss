import itertools
import pathlib
import re
import subprocess
import sys
import tempfile

import dwys

from invoke import task

import known

@task
def delenv(c):
    """
    Delete the conda environment created by `inv env`.
    """
    c.run("conda remove --name ampwoss --all")

@task
def env(c):
    """
    Finish the installation of any libraries and packages need for the
    environment.

    These are installation steps that are not able to be included in the
    anaconda environment file `environment.yml` (for example some R packages do
    not have anaconda binaries).
    """
    c.run(
        """Rscript -e 'install.packages("simmer", repos="http://cran.us.r-project.org")'"""
    )
    c.run(
        """Rscript -e 'install.packages("expm", repos="http://cran.us.r-project.org")'"""
    )


@task
def compile(c):
    """
    Compile the LaTeX document.
    """
    c.run("cd src; latexmk  -interaction=nonstopmode  --xelatex -shell-escape main.tex")

@task
def analyse(c):
    """
    Analyse the document style and wording.

    This makes use of the `diction` and `style` packages.

    Installation:

        Linux:

            apt install diction
            apt install style

        OS X:

            brew install diction
            brew install style
    """
    book = list(pathlib.Path("./src/").glob("**/*.tex"))
    for path in book:
        print(path)
        c.run(f"detex {path} | diction -s -L en_gb")
        c.run(f"detex {path} | style -L en_gb")

@task
def doctest(c, style=False):
    """
    Run doctests on all LaTeX documents

    - Checks code gives expected output using dwys
    - Check style of python code with black
    - Check style of R code with lintr (TODO Check that this works)
    """
    max_column_length = 63
    pyin_pattern = re.compile(r"\\begin\{pyin\}\n(.*?)\\end\{pyin\}", re.DOTALL)
    pyout_pattern = re.compile(r"\\begin\{pyout\}\n(.*?)\n\\end\{pyout\}", re.DOTALL)
    Rin_pattern = re.compile(r"\\begin\{Rin\}\n(.*?)\\end\{Rin\}", re.DOTALL)
    Rout_pattern = re.compile(r"\\begin\{Rout\}\n(.*?)\n\\end\{Rout\}", re.DOTALL)
    pyexecution_command = "python"
    Rexecution_command = "Rscript"

    book = list(pathlib.Path("./src/").glob("**/*.tex"))
    dir_for_python_input_files = tempfile.mkdtemp()
    dir_for_R_input_files = tempfile.mkdtemp()

    exit_codes = []
    for i, p in enumerate(book):
        print(f"Testing {p}")
        text = p.read_text()

        for in_pattern, out_pattern, execution_command, input_dir in (
            (
                pyin_pattern,
                pyout_pattern,
                pyexecution_command,
                dir_for_python_input_files,
            ),
            (Rin_pattern, Rout_pattern, Rexecution_command, dir_for_R_input_files),
        ):
            # Parse the code
            input_code, output_code = dwys.parse(
                string=text, in_pattern=in_pattern, out_pattern=out_pattern
            )

            if execution_command == "python":
                input_filename = f"{dir_for_python_input_files}/{i}.py"
            else:
                input_filename = f"{dir_for_R_input_files}/{i}.R"

            try:
                diff, output, expected_output = dwys.diff(
                    input_code=input_code,
                    expected_output_code=output_code,
                    execution_command=execution_command,
                    input_filename=input_filename,
                )
                diff = list(diff)

                try:
                    assert diff == []
                    exit_codes.append(0)
                    print(f"{execution_command}: ✅")
                except AssertionError:
                    print(f"{execution_command}: ❌ Input does not match output in {p}")
                    print(f"Obtained output:\n{output}")
                    print(f"Expected output:\n{expected_output}")
                    exit_codes.append(1)

            except AssertionError:
                print(f"{execution_command}: ❌ Syntax error in {p}")
                print(input_filename)
                print(subprocess.check_output([execution_command, input_filename]))
                exit_codes.append(1)

    print("Ensuring column lengths fit book")
    for path in itertools.chain(
        pathlib.Path(dir_for_R_input_files).glob("*"),
        pathlib.Path(dir_for_python_input_files).glob("*"),
    ):
        lines = path.read_text().split("\n")
        for line in lines:
            if len(line) > max_column_length:
                print(
                    f"'{line[:max_column_length]}' is too long ({len(line)} > {max_column_length})"
                )
                exit_codes.append(1)

    print("Check spelling")
    for path in book:
        latex = path.read_text()
        aspell_output = subprocess.check_output(
            ["aspell", "-t", "--list", "--lang=en_GB"], input=latex, text=True
        )
        incorrect_words = set(aspell_output.split("\n")) - {""} - known.words
        if len(incorrect_words) > 0:
            print(f"In {path} the following words are not known: ")
            for string in sorted(incorrect_words):
                print(string)
            exit_codes.append(1)

    if style is True:
        exit_codes += check_style(dir_for_python_input_files, dir_for_R_input_files)

    exit_code = max(exit_codes)
    if exit_code == 0:
        print("✅✅✅ ALL TESTS HAVE PASSED! ✅✅✅")
    else:
        print("❌❌❌ A test has failed. ❌❌❌")
    sys.exit(exit_code)

def check_style(dir_for_python_input_files, dir_for_R_input_files):
    exit_codes = []
    print("Running black")
    ec = subprocess.call(
        ["black", "--check", "--diff", "-l 63", dir_for_python_input_files]
    )
    exit_codes.append(ec)

    print("Running docformatter")
    ec = subprocess.call(
        [
            "docformatter",
            "--check",
            "--wrap-descriptions",
            "63",
            "--wrap-summaries",
            "63",
            "-r",
            dir_for_python_input_files,
        ]
    )
    if ec > 0:
        diff = subprocess.check_output(
            [
                "docformatter",
                "--wrap-descriptions",
                "63",
                "--wrap-summaries",
                "63",
                "-r",
                dir_for_python_input_files,
            ]
        )
        print(diff.decode("utf-8"))
    else:
        print("Docstrings follow PEP 257 ✅")
    exit_codes.append(min(ec, 1))

    print("Running lintr")
    # This excludes one specific lintr called 'object_usage_linter' as this is a
    # known issue with the lintr package in R.
    for path in pathlib.Path(dir_for_R_input_files).glob("*"):
        output = subprocess.check_output(
            [
                "Rscript",
                "-e",
                f"lintr::lint('{path}', linters=lintr::default_linters[names(lintr::default_linters) != 'object_usage_linter'])",
            ]
        )
        if len(output) > 0:
            print(output.decode("utf-8"))
            exit_codes.append(1)
    return exit_codes
