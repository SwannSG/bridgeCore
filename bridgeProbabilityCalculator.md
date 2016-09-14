# Bridge probability Calculations

## Basic Building Blocks

How many ways can we select *n* items from a large collection of *N* objects. The first item we select, we choose from *N* obects, then when that object is taken, we can choose from *N - 1* objects, and so on.

\#ways to choose n items = N x N-1 x N-2 .... up to n terms.

Now if we consider the set {a,b} to be the same as {b,a}, where a and b are items drawn from N. Note the set can have length *n*, and in this case n=2. If we only want unique sets, how do we remove these "duplicates" from *#ways to choose n items*.

Well we need to "cancel these duplicates out" by dividing by the number of ways *n* objects can be arranged.

\#number of ways n items can be arranged = n!

$$\alpha$$
