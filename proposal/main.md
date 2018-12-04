# CRC Focus Proposal

## TITLE AND AUTHOR(S)

### 1. Provisional title of your book.

"Applied mathematics with Open Source Software: Operational Research problems
with Python and R."

### 2. Author(s)/editor(s), affiliations and contact information

- Name: Vincent Knight and Geraint Palmer
- Affiliation: Cardiff University School of Mathematics
- Address: Mathematics Institute, Senghennydd Road, Cardiff, CF24 4AG
- Telephone: +44 (0)29 2087 5548
- Email: knightva@cardiff.ac.uk and palmergi1@cardiff.ac.uk

## Subject, aims and features

### 3. Please describe in detail the subject of your book and indicate its academic level.

This book will cover an overview of Operational Research problem with a
specific emphasis on solving them with open source software. The academic level
will be from undergraduate to postgraduate students and researchers either
aiming to learn about Operational Research and/or wanting to solve applied
problems using open tools.


The typical chapter structure will be:

1. Introduction - a brief overview of a given problem type.
2. Example problem.
3. Solving with Python.
4. Solving with R.
5. Brief theoretic background with pointers to reference texts.
6. Examples of research using these methods.

The topics covered will span the common range of Operational Research problems:
from the basics of probabilistic modelling to more niche areas such as linear
programming and game theory. See additional materials for further details.


### 4. Please describe your motivation for writing the book; why it is important.


There are numerous texts that cover the theoretic background of the field of
Operational Research. Numerous undergraduate and postgraduate courses in these
fields make use of these texts but also complement them with the use of
commercial software. Students are often left with the misconception that a
particular topic is equivalent to the particular commercial software product
that was used during the course. This is unnecessary and also not inclusive of
those unable to afford these products. Furthermore, it does not promote open
research best practice.

This book will offer a very important resource: showcasing how the numerous
areas of applied mathematical problem solving can be done using free and open
tools.


### 5. Please list up to 5 key features of your proposed book.

1. Full description and setup instructions for use of open source software.
2. Theoretic description of a number of mathematical problem solving tools.
3. Clear and detailed code examples in one or when appropriate two open source
   programming languages.
4. Discussion of research carried out in each topic.


### 6. Will your book feature any supplementary material, e.g. code and datasets online?

The source files for the book itself (the LaTeX files) and the programming
examples will be open sourced. This will also ensure that usable code will be
available.

## Audience and related books

### 7. Please discuss the intended audience for your book. Is it written primarily for scholars (if so, what disciplines), professionals (if so, which fields), or students (if so, what level)? Please be as specific and realistic as possible and remember that few, if any, books appeal to all of the above simultaneously.

The intended audience will be scholars of applied mathematics and/or
operational research. The intention of the book is to give an overview of the
theoretic background of each type of problem considered but details of the
actual implementation process will be the highlight of each chapter. Thus, this
will be of interest to students (undergraduate and/or postgraduate) as well as
academics who want to learn how to use open source software.


### 8. Please list below published books (or online resources) which one might consider as similar to your own: on the same topic, written at the same level, and intended for the same audience.  If you feel there is no direct competition for your book, please list those titles that are more generally related to your book.


- "Python for conducting operational research in healthcare":
  https://www.youtube.com/watch?v=CcEURL392-w The proposed text will differ from
  this talk by providing a text based resource but also by expanding to include
  further areas of operational research.
- Allen Downey's "Think complexity" http://greenteapress.com/complexity/ and
  other similar titles. The proposed text will differ from this in its main
  message, whilst Allen Downey's books aim to use programming to teach concepts,
  the proposed text will concentrate on implementation of concepts.
- Taha's "Operations Research: An Introduction, Global Edition"
  https://www.amazon.co.uk/Operations-Research-Introduction-Hamdy-Taha/dp/1292165545/ref=sr_1_1?ie=UTF8&qid=1543934254&sr=8-1&keywords=operational+research.
  The proposed text will actually complement these sorts of general texts quite
  while by showing implementation of the concepts using open source software.
- Jones, Maillardet and Robinson's "Introduction to Scientific Programming and
  Simulation Using R (Chapman & Hall/CRC: The R Series)"
  https://www.amazon.co.uk/Introduction-Scientific-Programming-Simulation-Chapman/dp/1466569999/ref=sr_1_2?s=books&ie=UTF8&qid=1543934328&sr=1-2&keywords=Owen+Jones+R.
  The proposed text will differ from this as it will concentrate on two
  programming languages, thus hopefully showcasing the implementation as a
  general concept. Furthermore, the proposed text will be briefer in its form
  aiming to provide a handbook like experience to readers.
- "Python for healthcare analytics and modelling" https://pythonhealthcare.org/.
  The proposed text differs from this by offering a more general text, both in
  terms of programming language but also in terms of the subjects considered.


## FURTHER DETAILS

### 9. Roughly how many thousand words in length will your book be? CRC Focus books are 20,000 to 50,000 words long, including references and footnotes.

40,000 words.

### 10. When would you hope to be able to submit the final draft of the book to us? And in which format, LaTeX or Word?

LaTeX

### 11. Please give the names and e-mail addresses of five people who would be qualified to give an opinion on your proposed book. (We will not necessarily contact these people).

- Allen Downey: downey@allendowney.com
- Thomas Monks: thomas.monks@soton.ac.uk
- Paul Harper: harper@cardiff.ac.uk
- Sally Brailsford: S.C.Brailsford@soton.ac.uk
- Sally McClean: si.mcclean@ulster.ac.uk

### 12. Which scholarly/professional societies are applicable for marketing your book?

Operational research societies such as:

- INFORMS: https://www.informs.org/
- The OR Society: https://www.theorsociety.com/

More general mathematical societies:

- IMA: https://ima.org.uk/
- SIAM: https://www.siam.org/
- AMS: https://www.ams.org/

Research software communities:

- SSI: https://www.software.ac.uk/

### 13. Please include a full table of contents, including chapter sub-headings and/or chapter abstracts. If the book is an edited collection, please also provide a tentative list of the expected authors and their affiliations (it is not necessary to have gained agreement from these people to contribute at this time). 

---

###### Chapter 1. Introduction

This chapter will introduce the book: describing what is to be considered an
applied mathematical problem. The origins of Operational Research. This chapter
will also describe the origins of open source software and give a number of
examples of them.

###### Chapter 2. Basic programming and the command line

This chapter will describe the installation and setup of Anaconda. It will also
describe using the command line as an interface to your computer. Finally, some
basics of Python and R (two open source languages) will also be covered.

##### Part 1: Probabilistic modelling

###### Chapter 3. Markov chains

This chapter will describe probabilistic modelling with Markov chains: the
basic theory will be covered. An example of modelling a queue will be used.
Python/R will be used to illustrate building the continuous time transition
matrix, discretizing it, looking at the long run time and finding the steady
state vector. Some what if scenarios will be considered. Finally a discussion
of some research using these notions will be used.


###### Chapter 4. Discrete event simulation

In a similar fashion to Chapter 8: some queueing network problems cannot be
easily computed as a Markov chain. This chapter will describe the theoretic
background of discrete event simulation. It will illustrate the simulation of a
complex queuing network using Python/R. Further examples of Research in this
area will be described.

##### Part 2: Dynamical systems

###### Chapter 5. Modelling with differential equations

This chapter will describe using differential equations to model real world
systems. A theoretic background will be included and symbolic computations (in
Python/R) will be used to solve differential equations exactly. The example of
Lanchester's battle equations will be used. A discussion of research on these
topics will be included.

###### Chapter 6. Systems dynamics

This chapter will describe the numerical solution of a dynamical system: for
some systems of differential equations, obtaining exact solutions is too complex
in which case they can be solved numerically. An example of modelling the spread
of disease in a complex format will be used. Python/R will be used to build the
underlying equations and solve them numerically. Some what if scenarios will be
considered.  Finally a discussion of some research using these notions will be
used.

##### Part 3: Emergent behaviour

###### Chapter 7. Game theory

This will describe basics of game theory: theoretic background to concepts of
equilibria will be described.  A game modelling interactions between two
transport providers (or something) will be considered. Python/R will be used to
obtain the Nash equilibria. A discussion of some research using these notions
will be used.

###### Chapter 8. Agent based simulation

Notions of Agent based simulation will be used. As an example Schelling’s model
of segregation will be built using Python/R. Research in this area will also be
described. (Capture relationships with networkX).


##### Part 4: Optimisation

###### Chapter 9. Linear programming

This chapter will describe the optimisation of a linear programme: the basic
theory will be covered. An example of scheduling exams will be illustrated,
Python/R will be used to build the LP and solve it. A discussion of some
research using these notions will be used.


###### Chapter 10. Heuristics

Some optimisation problems cannot be solved exactly: for example the TSP. The
basic theory will be covered. An example of solving the TSP using heuristic
optimisation algorithms in Python/R will be covered. Further examples of this in
research will be discussed.

##### Appendix: Data analysis, machine learning and statistics

Numerous texts cover the Data analysis with Python/R, this chapter will give a
very brief overview of these and give a description of good texts on the
subject.

---

#### 16. Please include a brief biography for each author/editor. (N.B. biographies are not required for contributors).


Vince Knight is a senior lecturer (associate professor) of Mathematics at
Cardiff University. He is a maintainer of open source libraries used in agent
based modelling and game theoretic research. He is a fellow of the
sustainable software institute highlighting his interest in best practice when
it comes to scientific programming. He has been teaching programming for more
than 10 years and is regularly involved in organising Python conferences in the
UK and Africa.

Geraint Palmer is a teaching associate of Mathematics at Cardiff University. He
is a maintainer of an open source library for discrete event simulation. He is
also a fellow of the sustainable software institute and has presented at a
number of international conference on the subject of best practice of scientific
computing. He has used open software tools in his own research and regularly
teaches programming.
