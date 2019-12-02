# ampwoss

Applied mathematics problems with Open Source Software: Operational Research with Python and R.

## Create the Conda environment:

Assuming you have anaconda on your machine, run:

    $ conda env create -f environment.yml

There are some further dependencies that are needed.

Activate the environment:

    $ conda activate amwpwoss
    $ inv env

## Compilation instructions

Run:

    $ inv compile

## Doctesting

Run:

    $ inv doctest

## Analysing the document

Run:

    $ inv analyse

This analyses the tex documents with `style` and `diction`:

- `style`: analyses surface characteristics of a document, including sentence
  length and other readability measures.
- `diction`: identifies wordy and commonly misused phrases.

See
http://wiki.christophchamp.com/index.php?title=Style_and_Diction#Lix
for more information.

To install these packages:

    Debian:

        apt install diction
        apt install style

    OS X (with the brew package manager):

        brew install diction
        brew install style
