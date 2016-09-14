# Bridge probability Calculations

## Basic Building Blocks

How many ways can we select n items from a large collection of N objects. For the first time we select we can choose from N obects, then when that object is taken, we can choose from N - 1 objects, and so on.

\#ways to choose n items = N * N-1 * N-2 .... up to n terms.

Now if we consider the set {a,b} to be the same as {b,a}, where a and b are items drwan from N. Note the set can have length *n*. And we only want unique sets, how do we remove these duplicates from *#ways to choose n items*.

Well we need to "cancel these duplicates out" by dividing by the number of ways n objects can be arranged.

\frac{n!}{k!(n-k)!}