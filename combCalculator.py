import math
import itertools
from functools import reduce


def termValue(s):
    """
        s has form 'A|K|Q|J0|1|2|3|4'
        return integer 
    """
    global HCP
    return HCP[s[0]] * int(s[1])


def C(n, N):
    # unique ways to choose n items from N objects
    return math.factorial(N)/(math.factorial(N-n)*math.factorial(n))


def hcp_combos(condition, value):
    """
    condition: '=|>|<'
    value:     0 <= integer <= 40
    returns list of tuples, each tuple has unique combination of aces, kings, queens, jacks to achieve hcp range 
    """
    global AN, KN, QN, JN
    result = []
    if condition=='=':
        for r in itertools.product(AN, KN, QN, JN):
            if termValue(r[0]) + termValue(r[1]) + termValue(r[2]) + termValue(r[3]) == value:
                result.append(r)
    elif condition=='>':
        for r in itertools.product(AN, KN, QN, JN):
            if termValue(r[0]) + termValue(r[1]) + termValue(r[2]) + termValue(r[3]) > value:
                result.append(r)
    elif condition=='<':
        for r in itertools.product(AN, KN, QN, JN):
            if termValue(r[0]) + termValue(r[1]) + termValue(r[2]) + termValue(r[3]) < value:
                result.append(r)
    return result


HCP = {}
HCP['A'] = 4
HCP['K'] = 3
HCP['Q'] = 2
HCP['J'] = 1


AN = ['A0', 'A1', 'A2', 'A3', 'A4']
KN = ['K0', 'K1', 'K2', 'K3', 'K4']
QN = ['Q0', 'Q1', 'Q2', 'Q3', 'Q4']
JN = ['J0', 'J1', 'J2', 'J3', 'J4']


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

# prob hand contains exactly x points 

x = 1
hcp_combo = hcp_combos('=', x)
cmd = 'cmd_result = '
for each in hcp_combo:
    print (each)
    honors = int(each[0][1]) + int(each[1][1]) + int(each[2][1]) + int(each[3][1])
    cmd = cmd + \
          'C(' + str(each[0][1]) + ',4) * ' + \
          'C(' + str(each[1][1]) + ',4) * ' + \
          'C(' + str(each[2][1]) + ',4) * ' + \
          'C(' + str(each[3][1]) + ',4) * ' + \
          'C(' + str((13 - honors)) + ',36) + '
cmd = cmd[:-3]
print (cmd)
exec(cmd)
r9 = cmd_result/nt


# prob hand contains 1 point and specific 5-3-3-2 distribution

# honor in spades
r_1 = C(1,1)*C(4,12)*C(3,13)*C(3,13)*C(2,13)

# honor in hearts
r_2 = C(5,13)*C(1,1)*C(2,12)*C(3,13)*C(2,13)

# honor in diamonds
r_3 = C(5,13)*C(3,13)*C(1,1)*C(2,12)*C(2,13)

# honor in clubs
r_4 = C(5,13)*C(3,13)*C(1,13)*C(1,1)*C(1,12)

r_0 = r_1 + r_2 + r_3 + r_4


# end Single Hand ********************************


# Your hand and partner's hand

# number of dual hands
r20 = C(13,39)







