# ampwoss

Applied mathematics problems with Open Source Software: Operational Research
with Python and R.

## Back Cover

Talk about distinct parts.

## Chapter abstracts

### Chapter 1: Introduction

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
should be made to offset the lose of productivity.

A theoretic overview of what a differential equation is and what a solution of a
differential equation represents is given.

The solution offered in Python is done symbolically using the Sympy library
whereas the solution offered in R is done through numerical integration using
deSolve.

### Chapter 5: System dynamics

This chapter models the spread within a population of an infectious disease as a
compartmental model. The goal is to understand what interventions could be made
to help minimise the long term effects of the disease.

A theoretic overview of systems of ordinary differential equations is presented
in terms of stocks and taps. The specific model used here: an SIR model is
discussed in detail. This is all complemented with a brief discussion of some
numerical techniques used to numerically integrate systems of ordinary
differential equations.

The solution offered in Python makes use of Numpy and Scipy which is equivalent
to the solution offered in R which makes use of deSolve.

## Chapter 6:

This chapters models a policy decision that has implications on the actions of
two companies in a duopoly is modeled as a normal form game. The goal is to
understand what financial incentives can be put in place to ensure competition
between the companies that benefits the consumer.

A theoretic overview of the definition of normal form games and Nash equilibrium
is given. Some discussion of other concepts such as learning algorithms and
evolutionary game theory are also included.

The solution offered in Python makes use of Nashpy which is a specific library
for the computation of Nash equilibria. The solution offered in R makes use of
Recon which is a general purpose library with functionality for a few topics in
economics.

## Chapter 7:

This chapters models a population of association football fans as a classic
agent based model of segregation. The goal is to understand how the individual
preferences of the population members affects the overall observed behaviour at
the population level.

A theoretic overview of agent based modelling is given specifically
concentrating on the roles of agents and the environment.

Python is a fully object oriented programming language and so no libraries are
used: agents and the environment are written as specific classes with all the
required functionality. The R solution makes use of the R6 library which allows
for a similar implementation of classes with required functionality.


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
