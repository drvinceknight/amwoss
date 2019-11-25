import pathlib
import re
import subprocess
import tempfile
import sys

import dwys

from invoke import task


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
def doctest(c):
    """
    Run doctests on all LaTeX documents

    - Checks code gives expected output using dwys
    - Check style of python code with black
    - Check style of R code with lintr (TODO Check that this works)
    """
    pyin_pattern = re.compile(r"\\begin\{pyin\}\n(.*?)\\end\{pyin\}", re.DOTALL)
    pyout_pattern = re.compile(r"\\begin\{pyout\}\n(.*?)\n\\end\{pyout\}", re.DOTALL)
    Rin_pattern = re.compile(r"\\begin\{Rin\}\n(.*?)\\end\{Rin\}", re.DOTALL)
    Rout_pattern = re.compile(r"\\begin\{Rout\}\n(.*?)\n\\end\{Rout\}", re.DOTALL)
    pyexecution_command = "python"
    Rexecution_command = "Rscript"

    book = pathlib.Path("./src/").glob("**/*tex")
    dir_for_python_input_files = tempfile.mkdtemp()
    dir_for_R_input_files = tempfile.mkdtemp()

    exit_codes = []
    for i, p in enumerate(book):
        if p.suffix == ".tex":
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
                        print(
                            f"{execution_command}: ❌ Input does not match output in {p}"
                        )
                        print(f"Obtained output:\n{output}")
                        print(f"Expected output:\n{expected_output}")
                        print(f"\t {diff}")
                        exit_codes.append(1)

                except AssertionError:
                    print(f"{execution_command}: ❌ Syntax error in {p}")
                    print(input_filename)
                    exit_codes.append(1)

    print("Running black")
    ec = subprocess.call(["black", "--check", "--diff", dir_for_python_input_files])
    exit_codes.append(ec)

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
    sys.exit(max(exit_codes))
