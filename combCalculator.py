# Bridge probability calculator

import math

def C(n, N):
    """
        Binomial coefficient
        normaly refered to as "n choose k"
        I prefer (small) n from (big) N, then n->k and N->n
    """
    return math.factorial(N)/(math.factorial(N-n)*math.factorial(n))

# Single Hand ************************************

# total number of hands that can be dealt
nt = C(13, 52)

# choose a hand with all top honors
r0 = C(4,4)*C(4,4)*C(4,4)*C(1,4)/nt

# choose a hand with 5-3-3-2 generic distribution
r1 = C(5,13)*C(3,13)*C(3,13)*C(2,13)

# choose a hand with no Aces
r2 = C(0,4)*C(13,48)

# probability that a bridge hand contains the ace of spades
r3 = C(1,1)*C(12,51)/nt

# probability hand contains all four aces
r4 = C(4,4) * C(9,48) /nt

# prob hand contains exactly two  aces
r5 = C(2,4) * C(11, 48) / nt

# choose a hand with all of one suit
r6 = (C(13,13)*C(0,39) + C(13,13)*C(0,39) + C(13,13)*C(0,39) + C(13,13)*C(0,39))/nt

# 12 card suit, Ace high
r7 = 4*C(11,12)*C(1,1)*C(1,36)/nt

# nine honors
r8 = C(9,20)*C(4,32)/nt

# end Single Hand ********************************


# Your hand and partner's hand

# number of dual hands
r20 = C(13,39)
