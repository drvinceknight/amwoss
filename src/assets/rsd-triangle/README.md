A diagram showing the relationship between modularisation, documentation and
testing. Used in the introductory chapter to describe how the code is written in
the book.

## To compile

To compile the LaTeX document:

    $ latexmk --xelatex main.tex

To convert `main.pdf` to `png`:

    $ convert -density 300 main.pdf -quality 90 main.png
