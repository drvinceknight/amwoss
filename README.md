# ampwoss

Applied mathematics problems with Open Source Software: Operational Research with Python and R.

## Compilation instructions

Run:

    $ latexmk --xelatex -shell-escape main.tex

## Doctesting

Create the conda environment from file.

    conda env create -f environment.yml

Activate the conda environment:

    conda activate ampwoss

Run the doctest suite:

    python main.py
