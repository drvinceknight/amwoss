# Editorial principles

## Who is this book for?
This book is aimed at readers who want to use open source software to solve the
considered applied mathematical problems. Some knowledge of mathematics is
assumed but is not necessary. 
It is also assumed that the reader will have done any introductory tutorial in R
or Python.
TODO Add pointer to such tutorials
	
By reading a particular chapter of the book, the reader will have:
	
\begin{enumerate}
  \item the practical knowledge to solve problems using a computer,
  \item an overview of the higher level theoretic concepts,
  \item pointers to further reading to gain background understand and research
  undertaken using the concepts.
\end{enumerate}

## Contents of sections

### Introduction

> If I know nothing about the topic and read this paragraph I will know a
> surface description of the problem type and the name of the solution approach.
> Typically 2 or 3 sentences.

### Typical Problem

> A brief (but comprehensive) description of a typical problem. If I do not know
> anything about the subject matter I can understand the problem and the problem
> parameters. If I **do** know the subject matter I should be able to solve the
> problem.

### Theory

- Typically there are two things to cover in this section (these might not
  necessarily be separate): 
	    1. A  comprehensive (but not in depth) overview of the theory.
	    2. How the theory applies to our typical problem
	- Can assume a secondary education in mathematics.
	- Concepts that are taught in a typical University mathematics course can be
	  assumed but should include reference texts as **footnotes**.
	-  Concepts that are **potentially** not taught in either of the above should
	   be introduced with gentle language, including potential subtle points at
	   programming section (eg "this can be done numerically") and reference
	   texts included as **footnotes**.
	- Use a smaller example (different to the typical problem) that can be done
	  by hand.
	- Some theoretic concepts might be illustrated using the typical problem.


### Code

- Give a brief (blog post style) overview of using each langauge to solve the
problem. Possibly including smaller examples of code output.
- A functional approach is used: everything is embedded in functions that are
  called. Justification/explanation of this will be written in "about this book
  section" (documentation, modularity and testability are the justification).
  TODO Put in best practice triangle
- The two R and Python sections are **purposefully** written as near clones of
  each other. The alternative would be to write a single section with text that
  describes both the R and Python: however in multiple places this would need to
  clarify differences and similarities of implementation. This is not the
  purpose of the book thus there are two separate and independent sections. They
  are not written differently unless necessary.


#### Solving with Python

#### Solving with R

## Language

- Avoid we/I.
- In DES chapter we used digits for numbers (1, 2, 3 ... etc instead of one,
  two, three).
- Dice is plural, die is singular.
- Itemized, enumerated lists have `,` (or `;` if long) at the end and `.` at the
  end of the last
- In text: Names of libraries are in plain text and capitalized.

## Research highlights

> If I was undertaking a research project in this field, reading these three
> papers would be a good starting point to build the literature.
