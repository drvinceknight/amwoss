## Introduction & Background

In order to look at Markov modelling, consider the following problem.
I own a car, that can be in any one of five states: working normally (W),
overheating (O), being low on oil (L), both overheating and low on oil (OL), and
being broken down (B).
The car naturally deteriorates between these states with the following rates:

+ from W to O at rate 3,
+ from W to L at rate 3,
+ from W to B at rate 1,
+ from O to B at rate 8,
+ from O to OL ar rate 4,
+ from L to OL at rate 4,
+ and from L to B at rate 5.

I tend to check the oil of my car at rate 2, check the temperature of my car at
rate 3, and if I need to call a mechanice they will fix the car at rate 2:

+ from O to 

In states W, O, L and OL the car is able to be driven, but it cannot be driven
when in state B.
I'd like to know what percentage of the time my car will be undrivable?

We will model this using Markov chains.

This system can be written as the following matrix by ordering the states W, O,
L, OL and B:

$$
Q =
\begin{matrix}
-7 & 3 & 3 & 0 & 1 \\
3 & -15 & 0 & 4 & 8 \\
2 & 0 & -11 & 4 & 5 \\
0 & 2 & 2 & -16 & 12 \\
2 & 0 & 0 & & 0 & -2 \\
\end{matrix}
$$

So the rate of transitioning from the 1st state (W) to the second state (O) is
3, and so on.
Negative numbers are required in the diagonal which have their own
interpretation (discussed later).

Eventually the car will reach steady-state.


