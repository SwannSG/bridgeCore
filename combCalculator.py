import math
import itertools
from functools import reduce

def cin(number):
    # commasInNumber
    return "{:,}".format(number)


def gdToSd(gd):
    # generic distribution to list of specific distributions
    # gd: X-X-X-X
    gd = gd.split('-')
    return list(itertools.permutations(gd))
   

def spreadHC(t):
    """
        x = ('A0', 'K0', 'Q0', 'J1')
        returns ['J']
    """
    r = []
    for e in t:
        i = 0
        while i < int(e[1]):
            r.append(e[0])
            i = i + 1
    return r


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


def F(n):
    # factorial of a number
    return math.factorial(n)

def SF(n,l):
    # short factorial where l is the length
    return math.factorial(n)/math.factorial(n -l)
    

def isValid(r):
    """
        ('A4', 'K4', 'Q4', 'J4')    
        sum int(second_char)
        if sum <= 13 return True else False
    """
    temp = int(r[0][1]) + int(r[1][1]) + int(r[2][1]) + int(r[3][1])
    if temp<= 13:
        return True
    return False



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
                if isValid(r):
                    result.append(r)
    elif condition=='>':
        for r in itertools.product(AN, KN, QN, JN):
            if termValue(r[0]) + termValue(r[1]) + termValue(r[2]) + termValue(r[3]) > value:
                if isValid(r):
                    result.append(r)
    elif condition=='<':
        for r in itertools.product(AN, KN, QN, JN):
            if termValue(r[0]) + termValue(r[1]) + termValue(r[2]) + termValue(r[3]) < value:
                if isValid(r):
                    result.append(r)
    return result

def hcp_single_hand(condition, value):
    """
    condition: '=|>|<'
    value:     0 <= integer <= 40
    returns number of hands 
    """
    total_hands = 0
    hcp_combo = hcp_combos(condition, value)
    for each in hcp_combo:
        noOfHighCards = int(each[0][1]) + int(each[1][1]) + int(each[2][1]) + int(each[3][1])
        temp =  C(int(each[0][1]),4) * C(int(each[1][1]),4) * C(int(each[2][1]),4) * C(int(each[3][1]),4) * C(13 - noOfHighCards, 36) 
        total_hands = total_hands + temp
    return total_hands

def genericDistrHand(distr):
    """
        distr = 5-3-3-2
        result = C(5,13)*C(3,13)*C(3,13)*C(2,13)
        result: number of hands    
    """
    t = distr.split('-')
    return C(int(t[0]),13) * C(int(t[1]),13) * C(int(t[2]),13) * C(int(t[3]),13)
    

    



# CONSTANTS ***********************************************************

HCP = {}
HCP['A'] = 4
HCP['K'] = 3
HCP['Q'] = 2
HCP['J'] = 1


AN = ['A0', 'A1', 'A2', 'A3', 'A4']
KN = ['K0', 'K1', 'K2', 'K3', 'K4']
QN = ['Q0', 'Q1', 'Q2', 'Q3', 'Q4']
JN = ['J0', 'J1', 'J2', 'J3', 'J4']

GENERIC_DISTRIBUTIONS_HAND = ['13-0-0-0', '12-1-0-0', '11-2-0-0', '11-1-1-0', '10-3-0-0', '10-2-1-0', '10-1-1-1', '9-4-0-0', '9-3-1-0', '9-2-2-0', '9-2-1-1', '8-5-0-0', '8-4-1-0', '8-3-2-0', '8-3-1-1', '8-2-2-1', '7-6-0-0', '7-5-1-0', '7-4-2-0', '7-4-1-1', '7-3-3-0', '7-3-2-1', '7-2-2-2', '6-6-1-0', '6-5-2-0', '6-5-1-1', '6-4-3-0', '6-4-2-1', '6-3-3-1', '6-3-2-2', '5-5-3-0', '5-5-2-1', '5-4-4-0', '5-4-3-1', '5-4-2-2', '5-3-3-2', '4-4-4-1', '4-4-3-2', '4-3-3-3']

GENERIC_DISTRIBUTIONS_TWO_HANDS = ['26-0-0-0', '25-1-0-0', '24-2-0-0', '24-1-1-0', '23-3-0-0', '23-2-1-0', '23-1-1-1', '22-4-0-0', '22-3-1-0', '22-2-2-0', '22-2-1-1', '21-5-0-0', '21-4-1-0', '21-3-2-0', '21-3-1-1', '21-2-2-1', '20-6-0-0', '20-5-1-0', '20-4-2-0', '20-4-1-1', '20-3-3-0', '20-3-2-1', '20-2-2-2', '19-7-0-0', '19-6-1-0', '19-5-2-0', '19-5-1-1', '19-4-3-0', '19-4-2-1', '19-3-3-1', '19-3-2-2', '18-8-0-0', '18-7-1-0', '18-6-2-0', '18-6-1-1', '18-5-3-0', '18-5-2-1', '18-4-4-0', '18-4-3-1', '18-4-2-2', '18-3-3-2', '17-9-0-0', '17-8-1-0', '17-7-2-0', '17-7-1-1', '17-6-3-0', '17-6-2-1', '17-5-4-0', '17-5-3-1', '17-5-2-2', '17-4-4-1', '17-4-3-2', '17-3-3-3', '16-10-0-0', '16-9-1-0', '16-8-2-0', '16-8-1-1', '16-7-3-0', '16-7-2-1', '16-6-4-0', '16-6-3-1', '16-6-2-2', '16-5-5-0', '16-5-4-1', '16-5-3-2', '16-4-4-2', '16-4-3-3', '15-11-0-0', '15-10-1-0', '15-9-2-0', '15-9-1-1', '15-8-3-0', '15-8-2-1', '15-7-4-0', '15-7-3-1', '15-7-2-2', '15-6-5-0', '15-6-4-1', '15-6-3-2', '15-5-5-1', '15-5-4-2', '15-5-3-3', '15-4-4-3', '14-12-0-0', '14-11-1-0', '14-10-2-0', '14-10-1-1', '14-9-3-0', '14-9-2-1', '14-8-4-0', '14-8-3-1', '14-8-2-2', '14-7-5-0', '14-7-4-1', '14-7-3-2', '14-6-6-0', '14-6-5-1', '14-6-4-2', '14-6-3-3', '14-5-5-2', '14-5-4-3', '14-4-4-4', '13-13-0-0', '13-12-1-0', '13-11-2-0', '13-11-1-1', '13-10-3-0', '13-10-2-1', '13-9-4-0', '13-9-3-1', '13-9-2-2', '13-8-5-0', '13-8-4-1', '13-8-3-2', '13-7-6-0', '13-7-5-1', '13-7-4-2', '13-7-3-3', '13-6-6-1', '13-6-5-2', '13-6-4-3', '13-5-5-3', '13-5-4-4', '12-12-2-0', '12-12-1-1', '12-11-3-0', '12-11-2-1', '12-10-4-0', '12-10-3-1', '12-10-2-2', '12-9-5-0', '12-9-4-1', '12-9-3-2', '12-8-6-0', '12-8-5-1', '12-8-4-2', '12-8-3-3', '12-7-7-0', '12-7-6-1', '12-7-5-2', '12-7-4-3', '12-6-6-2', '12-6-5-3', '12-6-4-4', '12-5-5-4', '11-11-4-0', '11-11-3-1', '11-11-2-2', '11-10-5-0', '11-10-4-1', '11-10-3-2', '11-9-6-0', '11-9-5-1', '11-9-4-2', '11-9-3-3', '11-8-7-0', '11-8-6-1', '11-8-5-2', '11-8-4-3', '11-7-7-1', '11-7-6-2', '11-7-5-3', '11-7-4-4', '11-6-6-3', '11-6-5-4', '11-5-5-5', '10-10-6-0', '10-10-5-1', '10-10-4-2', '10-10-3-3', '10-9-7-0', '10-9-6-1', '10-9-5-2', '10-9-4-3', '10-8-8-0', '10-8-7-1', '10-8-6-2', '10-8-5-3', '10-8-4-4', '10-7-7-2', '10-7-6-3', '10-7-5-4', '10-6-6-4', '10-6-5-5', '9-9-8-0', '9-9-7-1', '9-9-6-2', '9-9-5-3', '9-9-4-4', '9-8-8-1', '9-8-7-2', '9-8-6-3', '9-8-5-4', '9-7-7-3', '9-7-6-4', '9-7-5-5', '9-6-6-5', '8-8-8-2', '8-8-7-3', '8-8-6-4', '8-8-5-5', '8-7-7-4', '8-7-6-5', '8-6-6-6', '7-7-7-5', '7-7-6-6']

SUIT_COMBO = [('S', 'H', 'D', 'C'), ('S', 'H', 'C', 'D'), ('S', 'D', 'H', 'C'), ('S', 'D', 'C', 'H'), ('S', 'C', 'H', 'D'), ('S', 'C', 'D', 'H'), ('H', 'S', 'D', 'C'), ('H', 'S', 'C', 'D'), ('H', 'D', 'S', 'C'), ('H', 'D', 'C', 'S'), ('H', 'C', 'S', 'D'), ('H', 'C', 'D', 'S'), ('D', 'S', 'H', 'C'), ('D', 'S', 'C', 'H'), ('D', 'H', 'S', 'C'), ('D', 'H', 'C', 'S'), ('D', 'C', 'S', 'H'), ('D', 'C', 'H', 'S'), ('C', 'S', 'H', 'D'), ('C', 'S', 'D', 'H'), ('C', 'H', 'S', 'D'), ('C', 'H', 'D', 'S'), ('C', 'D', 'S', 'H'), ('C', 'D', 'H', 'S')]

# end CONSTANTS *******************************************************


# Single Hand ************************************

# total number of hands that can be dealt
nt = C(13, 52)

# choose a hand with all top honors
r0 = C(4,4)*C(4,4)*C(4,4)*C(1,4)/nt

# choose a hand with 5-3-3-2 generic distribution
r1 = C(5,13)*C(3,13)*C(3,13)*C(2,13)

r1a = (SF(13,5)/F(5)) * (SF(13,3)/F(3)) * (SF(13,3)/F(3)) * (SF(13,2)/F(2))



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

r6a = 1/52 * 1/51 * 1/50 * 1/49 * 1/48 * 1/47 *1/46 * 1/45 * 1/44 * 1/43 * 1/42 * 1/41 * 1/40




# 12 card suit, Ace high
r7 = 4*C(11,12)*C(1,1)*C(1,36)/nt

# nine honors
r8 = C(9,20)*C(4,32)/nt

# choose a hand with 4-3-3-3 generic distribution
r9 = C(4,13)*C(3,13)*C(3,13)*C(3,13)
print (r9, genericDistrHand('4-3-3-3')) 




# prob hand contains x points 

"""
x = 30
condition = '<'
hcp_combo = hcp_combos(condition, x)
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
"""

#r9 = hcp_single_hand(condition, x)/nt



"""
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
"""

# hcp = 12 
print (hcp_single_hand('=', 12))


# hcp=1 and 4-3-3-3 distribution

# Try 1
# hcp=1 --> single Jack, which could be in any suit
# jack in spades
r11 = C(1,4)*C(3,9)*C(3,9)**3
# jack in hearts
r12 = C(4,9)*C(1,4)*C(2,9)*C(3,9)**2
# jack in diamonds
r12
# jack in clubs
r12
print (cin(r11), cin(r12))
avg = (r11 + 3*r12)/4
noOfHands = r11 + 3*r12
print (cin(avg))            # this gives the correct answer

#Ans = 583,220,736
# only 1 way Jack can go into 4-suit
r30 = C(1,4)*C(3,9)*C(3,9)**3
# 3 ways Jack can go into 3-suit
r31 = C(4,9)*C(1,4)*C(2,9)*C(3,9)**2






# hcp=0 and 4-3-3-3 distribution
r13 = C(4,9) * C(3,9)**3
print (cin(r13))

# hcp=2 and 4-3-3-3 distribution
# for single Queen
noOfHands
# for two Jacks
# one Jack in 4-card suit
r14 = C(1,4)*C(3,9) * C(1,3)*C(2,9) * C(3,9)**2
r14 = r14
# one Jack in each 3-card suit
r15 = C(4,9) * C(1,4)*C(2,9) * C(1,3)*C(2,9) * C(3,9)
r15 = r15

r16 = noOfHands + r14 + r15 # !!!Correct answer

print ('# hcp=2 and 4-3-3-3 distribution')
print (cin(r16))











# #hands with only 1 jack





# end Single Hand ********************************


# Your hand and partner's hand


# scratchpad

def groupHon(l):
    s = []
    h = []
    d = []
    c = []
    for e in l:
        if e[0]=='s':
            s.append(e[1])
        elif e[0]=='h':
            h.append(e[1])
        elif e[0]=='d':
            d.append(e[1])
        elif e[0]=='c':
            c.append(e[1])
    return (s, h, d, c)

def hcPlacement(bins, slots):
    # bins:  [('s0', 'J'), ('h0', 'J'), ('d0', 'J'), ('c0', 'J')]
    # slots: ['s0', 'h0', 'd0', 'c0']
    # result: [[('s0', 'J'), ('h0', None), ('d0', None), ('c0', None)],
    #         [('h0', 'J'), ('s0', None), ('d0', None), ('c0', None)],
    #         [('d0', 'J'), ('s0', None), ('h0', None), ('c0', None)],
    #         [('c0', 'J'), ('s0', None), ('h0', None), ('d0', None)]]

    result = []
    for each in bins:    
        x = each[0]
        row = []
        setDiff = set(slots) ^ set([x])
        row.append(each)
        for item in setDiff:
            row.append((item, None))
        result.append(row)
    return result

def flattenHC(hcpCombos):
    # hcpCombos: [('A0', 'K0', 'Q0', 'J1')]
    # result: ['J']
    final_result = []
    for each in hcpCombos:
        result = []
        for item in each:
            high_card = item[0]
            i = 0
            while i < int(item[1]):
                result.append(high_card)
                i = i + 1
        final_result.append(result)
    return final_result

def noName(slots, flatHC):
    # slots: ['s0', 'h0', 'd0', 'c0']
    # flatHC: [['J', 'J'], ['Q']]
    result = []
    for each in flatHC:
        temp = list(itertools.product(slots, each))
        print ('temp')
        print (temp)
        result.append(hcPlacement(temp, slots))
    return result


h = ['J']
s = ['s0', 'h0', 'd0', 'c0']
S = set(s)

o0 = list(itertools.product(s,h))
#[('s0', 'J'),[('s0', 'J'), ('h0', 'J'), ('d0', 'J'), ('c0', 'J')] ('h0', 'J'), ('d0', 'J'), ('c0', 'J')]

fr = []
for e in o0:
    slot = e[0]
    row = []
    ns = list(S ^ set([slot]))
    row.append(e)
    for index, item in enumerate(ns):
        row.append((item, None))            
    fr.append(row)


slots = ['s0', 'h0', 'd0', 'c0']
h = hcp_combos('=', 1)
h = flattenHC(h)

h = [['J', 'J']]
r14 = noName(slots, h)

for each in r14:
    print ('final result')
    for item in each:
        print (item)
        


b = list(itertools.permutations(slots))
r = set()
for each in b:
    li = [each[0], each[1]]
    print (li)
#    r.add(li)
          

# ***********************************
def combine(l1, l2):

    fr = []
    for each in l1:
        r = []
        i = 0
        while i < 4:
            r.append(each[i]+'-'+ l2[i])
            i = i + 1
        fr.append(r)
    return fr

p = list(itertools.permutations(slots))

r = combine(p, ['J', 'J', 'nJ', 'nJ'])




#bins = list(itertools.product(s,h))
#r14 = hcPlacement(bins, slots) 

    

"""
import numpy as np
a = np.chararray((1,4), unicode=True)
a[0,0]='s'
a[0,1]='h'
a[0,2]='d'
a[0,3]='c'
"""
