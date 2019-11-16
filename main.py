"""
Run doctests
"""
import pathlib
import re

import dwys

pyin_pattern = re.compile(r"\\begin\{pyin\}\n(.*?)\\end\{pyin\}", re.DOTALL)
pyout_pattern = re.compile(r"\\begin\{pyout\}\n(.*?)\n\\end\{pyout\}", re.DOTALL)
Rin_pattern = re.compile(r"\\begin\{Rin\}\n(.*?)\\end\{Rin\}", re.DOTALL)
Rout_pattern = re.compile(r"\\begin\{Rout\}\n(.*?)\n\\end\{Rout\}", re.DOTALL)
pyexecution_command = "python"
Rexecution_command = "Rscript"

book = pathlib.Path('./src/').glob('**/*tex')

for p in book:
    if p.suffix == ".tex":
        print(f"Testing {p}")
        text = p.read_text()

        for in_pattern, out_pattern, execution_command in (
                (pyin_pattern, pyout_pattern, pyexecution_command),
                (Rin_pattern, Rout_pattern, Rexecution_command)):
            # Parse the code
            input_code, output_code = dwys.parse(
                string=text, in_pattern=in_pattern, out_pattern=out_pattern
            )

            # Obtain a diff with the `Rscript` command
            try:
                diff, output, expected_output = dwys.diff(
                    input_code=input_code,
                    expected_output_code=output_code,
                    execution_command=execution_command,
                )
                diff = list(diff)
                try:
                    assert diff == []
                    print(f"{execution_command}: ✅")
                except AssertionError:
                    print(f"{execution_command}: Input does not match output in {p}")
                    print(f"Obtained output:\n{output}")
                    print(f"Expected output:\n{expected_output}")
                    print(f"\t {diff}")
            except AssertionError:
                print(f"{execution_command} Syntax error in {p}")
