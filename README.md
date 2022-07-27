# ampwoss

Applied mathematics problems with Open Source Software: Operational Research
with Python and R.

## Back Cover

**Applied Mathematics with Open-Source Software: Operational Research Problems
with Python and R** is aimed at a broad segment of readers who wish to learn how
to use open-source software to solve problems in applied mathematics.
The book has an innovative structure with 4 sections of two chapters covering a
large range of applied mathematical techniques: probabilistic modelling,
dynamical systems, emergent behaviour and optimisation. The pairs of chapters in
each section demonstrate different families of solution approaches. Each chapter
starts with a problem, gives an overview of the relevant theory, shows a
solution approach in R and in Python, and finally gives wider context by
including a number of published references. This structure will allow for maximum
accessibility, with minimal prerequisites in mathematics or programming as well
as giving the right opportunities for a reader wanting to delve deeper in to a
particular topic.

Features

- An excellent resource for scholars of applied mathematics and operational
  research, and indeed any academics who want to learn how to use open-source
  software.
- Offers more general and accessible treatment of the subject than other texts,
  both in terms of programming language but also in terms of the subjects
  considered.
- The R and Python sections purposefully mirror each other so that a reader can
  read only the section that interests them.
- An accompanying open source repository with source files and further
  examples.

## List of chapters

### Chapter 1: Introduction

This chapter aims to help a reader understand if this book is for them and what
background they need to use it. It starts by answering the following questions:

- Who is this book for?
- What is meant by applied mathematics?
- What is open source software?

The chapter structure of the book is then discussed, apart from the 1st chapter
all chapters have a similar structure and then some discussion is given to how
the code is written and presented.

This chapter can be skipped if a reader is confident in their use of programming
and wants to skip ahead to a specific problem.

### Chapter 2: Markov chains

This chapter models a barber shop as a queueing system using a continuous time
Markov chain. The goal is to identify which particular reconfiguration of the
barber shop would be most beneficial to customers.

A theoretic overview of concepts related to stationary distributions of
continuous Markov chains is given before solutions approaches are given in both
R and Python. This is done using Numpy in Python and expm in R for all the
underlying linear algebra.

- [Jupyter notebook example](./examples/ipynb/02/main.ipynb)

### Chapter 3: Discrete event simulation

This chapter models a bicycle repair shop as a network of two queueing
processes. The goal is to identify the effect of two particular improvements to
the service configuration.

A theoretic overview of two types of discrete event simulation frameworks is
given: event scheduling and process based simulation. As well as this the topics
of random processes and pseudorandom number generation are also covered.

The two types of simulation frameworks are addressed in the solution approaches:
in Python Ciw is used which is an implementation of event scheduling. In R
simmer is used which is an implementation of process based simulation.
As a result, perhaps this chapter more than any other is worthwhile reading both
the R and Python section (even if the reader is only a user of one language) as
this gives a good contrast to the two frameworks.

### Chapter 4: Differential equations

This chapter models the spread of a cold in a population as a single dimensional
problem. The goal is to identify whether or not an investment in cold medicine
should be made to offset a loss of productivity.

A theoretic overview of what a differential equation is and what a solution of a
differential equation represents is given.

The solution offered in Python is done symbolically using the Sympy library
whereas the solution offered in R is done through numerical integration using
deSolve.

### Chapter 5: System dynamics

This chapter models the spread of an infectious disease within a population  as a
compartmental model. The goal is to understand what interventions could be made
to help minimise the long term effects of the disease.

A theoretic overview of systems of ordinary differential equations is presented
in terms of stocks and flows. The specific model used here: an SIR model is
discussed in detail. This is all complemented with a brief discussion of some
numerical techniques used to integrate systems of ordinary
differential equations.

The solution offered in Python makes use of Numpy and Scipy which is equivalent
to the solution offered in R which makes use of deSolve.

## Chapter 6: Game theory

This chapters models a policy decision that has implications on the actions of
two companies in a duopoly modelled as a normal form game. The goal is to
understand what financial incentives can be put in place to ensure competition
between the companies that benefits the consumer.

A theoretic overview of the definition of normal form games and Nash equilibria
is given.

The solution offered in Python makes use of Nashpy which is a specific library
for the computation of Nash equilibria. The solution offered in R makes use of
Recon which is a general purpose library with functionality for a few topics in
economics.

## Chapter 7: Agent Based Simulation

This chapters models a population of association football fans as a classic
agent based model of segregation. The goal is to understand how the individual
preferences of the population members affects the overall observed behaviour at
the population level.

A theoretic overview of agent based modelling is given specifically
concentrating on the roles of agents and the environment.

In Python the fully object oriented nature of the language is used to model
agents and the environment as classes. The R solution makes use of the R6 library which allows
for a similar implementation of classes with required functionality.

## Chapter 8: Linear Programming

This chapter finds an exam schedule for a scenario where there are students that
have a number of possible clashes. This is done by formulating and solving a
linear programming problem.

A theoretic description of linear programming is given. Intuitive ideas that lead 
to solutions approaches  are described. Direct and linear algebraic formulations 
are explained.

The Python solution makes use of the Pulp library which corresponds to the
direct formulation of the problem. The R solution uses the ROI library which
requires the linear algebraic formulation.

## Chapter 9: Heuristics

This chapter identifies the best delivery route for a delivery company. This is
a traditional travelling salesman problem which aims to find a route that minimises 
the total distance travelled.

A theoretic description of neighbourhood search and a specific
consideration of the "2-opt" algorithm are given. These are types
of heuristic algorithms which may not
guarantee optimality but can often perform better in practice than exact
approaches.

The standard Python library and base R are used to build these algorithms.

# Biographies

Geraint Palmer is a Welsh Medium Lecturer at Cardiff University in the School of
Mathematics. He is a member of the operational research group where his research
interests are in simulation and probabilistic modelling, in particular applying
these to model public services such as healthcare systems. He uses open source
software in all aspects of his research: he is a maintainer of Ciw, an open source
Python library for discrete event simulation, and won the OR Society's Doctoral
Award in 2018. Geraint is also a fellow of the Software Sustainability Institute
and has presented at a number of international conferences on the subject of
best practice of scientific computing, and regularly teaches programming and
runs coding workshops for people of all ages.

Vince Knight is a Senior Lecturer at Cardiff University in the School of
Mathematics. His research interests are in emergent behaviour, probabilistic
modelling, applications in healthcare and pedagogy. He maintains a number of
open source research software projects, is a trustee of the UK Python
association, is an editor for the Journal of Open Source Software, was awarded
the 2017 John Pinner award for contribution to the Python community and is a
fellow of the Sustainable Software Institute. He regularly wins awards for his
teaching in the School of Mathematics. He does not only speak at conferences
around the world but continues to organise conferences to bring the
power of open source software to as many people as possible.

# Source fils

## Create the Conda environment:

Assuming you have anaconda on your machine, run:

    $ conda env create -f environment.yml

There are some further dependencies that are needed.

Activate the environment:

    $ conda activate ampwoss
    $ inv env

To delete the environment:

    $ inv delenv

## Compilation instructions

Run:

    $ inv compile

This creates a `build/` directory which contains slightly modified source files
(some annotations removed) as well as a `main.pdf`. This modifications are
prescribed by a `substitions` variables in `tasks.py`.

An intermediate step is to run:

    $ inv build

Which creates the modified source files but does not compile the document.

Note that as documented in
[#72](https://github.com/drvinceknight/amwoss/issues/142) the
`texlive-langgreek` latex package might be needed.

## Doctesting

Run:

    $ inv doctest

To doctest a specific chapter:

    $ inv doctest --path="src/chapters/06/main.tex"

To also check the style with `black` on the python code and `lintr` on
the R code:

    $ inv doctest --style

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
