# Bridge probability Calculations

## Basic Building Blocks

How many ways can we select *n* items from a large collection of *N* objects. The first item we select, we choose from *N* obects, then when that object is taken, we can choose from *N - 1* objects, and so on.

\#ways to choose n items = N x N-1 x N-2 .... up to n terms.

Now if we consider the set {a,b} to be the same as {b,a}, where a and b are items drawn from N. Note the set can have length *n*, and in this case n=2. If we only want unique sets, how do we remove these "duplicates" from *#ways to choose n items*.

Well we need to "cancel these duplicates out" by dividing by the number of ways *n* objects can be arranged.

\#ways n items can be arranged = n!

\#unique ways to choose n items = \#ways to choose n items / \#ways n items can be arranged  

This is implemented in a trivial Python function, as

```Python
def C(n, N):
    # unique ways to choose n items from N objects
    return math.factorial(N)/(math.factorial(N-n)*math.factorial(n))
```

### Total number of hands that can be dealt

Choose 13 cards from 52. This is the global space for all possible hands.  

\#hands = C(13,32)

### Number of hands with all top honors

We need 4 aces from 4 aces, 4 kings from 4 kings, 4 queens from 4 queens, and 1 jack from 4 jacks.

\#hands = C(4,4) x C(4,4) x C(4,4) x C(1,4)

### Choose a hand with 5-3-3-2 generic distribution

We need 5 cards from suit X, 3 cards from Y, 3 card from suit Z, and 2 cards from remaining suit.

\#hands =  C(5,13) x C(3,13) x C(3,13) x C(2,13)

### choose a hand with no Aces

We need 0 aces from 4 aces, and 13 cards from the remaining 48. C(0,X) is always one, and we include it just to show the logic.

\#hands = C(0,4) x C(13,48)

### probability that a bridge hand contains the ace of spades

We need 1 ace from 1 ace spades, and 12 cards from remaining 51.

\#hands = C(1,1) x C(12,51)

### probability hand contains all four aces

We need 4 aces from 4, and 9 cards from remaining 48.

\#hands = C(4,4) x C(9,48)

### prob hand contains exactly two  aces

We 2 aces from 4, and 11 cards from remaining 48.

\#hands = C(2,4) x C(11, 48)

# choose a hand with all of one suit

We need 13 cards from one suit of 13. But this can occur for each suit. Hence the addition.

\#hands = C(13,13) x C(0,39) + C(13,13) x C(0,39) + C(13,13) x C(0,39) + C(13,13) x C(0,39)

# 12 card suit, Ace high

We draw 12 cards from same suit of which one is the ace, and then 1 card from the rest which may not be an ace.
For say Spades suit we draw 11 from 12 (because we must exclude the ace), the 1 ace from 1 ace spades, and 1 card from balance of 36 (39 cards - 3 aces). And we need to do this for each suit. Hence the multiplication by 4.

\#hands = 4xC(11,12) x C(1,1) x C(1,36)

# nine honors

Here we include tens as honors, so there are 20 in total. We draw 9 from 20, and 4 from the balance of 32.

\#hands = C(9,20) x C(4,32)
