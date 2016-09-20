import math
import itertools
import operator

# nice presentation *******************************************************
def cin(n):
    # nice commas in big number
    # n is a number
    return "{:,}".format(n)

def percent(n):
    return str(n * 100) + '%'
# end nice presentation ***************************************************

# basic combination & permutation maths ***********************************
def C(n, N):
    # unique ways to choose n items from N objects
    if n==0:
        return 1.0
    return math.factorial(N)/(math.factorial(N-n)*math.factorial(n))

def F(n):
    # factorial of a number
    return math.factorial(n)

def SF(n,l):
    # short factorial where l is the length
    return math.factorial(n)/math.factorial(n -l)

def F(n):
    # factorial of a number
    return math.factorial(n)

def SF(n,l):
    # short factorial where l is the length
    # n=13, l=4 return 13 * 12 * 11 * 10
    return math.factorial(n)/math.factorial(n -l)

def A(n):
    # number of ways to arrange n items
    return F(n)
# end basic combination & permutation maths *******************************

# this section for distribution related stuff *****************************

def genericDistr_hands(genericDistr):
    # genericDistr: '4-4-3-2'
    # returns integer number of hands
    specificDistrCount = getSpecficDistrsCount(genericDistr)
    t = genericDistr.split('-')
    temp = C(int(t[0]),13)*C(int(t[1]),13)*C(int(t[2]),13)*C(int(t[3]),13)
    return temp * specificDistrCount

def getSpecficDistrs(genericDistr):
    # genericDistr: '4-4-3-2'
    # returns list of specific distributions related to the generic distribution 
    genericDistr = genericDistr.split('-')
    temp = list(set(list(itertools.permutations(genericDistr))))
    temp.sort(reverse=True)
    return temp

def getSpecficDistrsCount(genericDistr):
    # genericDistr: '4-4-3-2'
    # return integer, number of specific distributions related to the generic distribution 
    return len(getSpecficDistrs(genericDistr))    

# end this section for distribution related stuff *************************

# this section for HCP calculations ***************************************

def termValue(s):
    """
        s has form 'A|K|Q|J0|1|2|3|4'
        return integer 
    """
    global HCP
    return HCP[s[0]] * int(s[1])

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

def hcp_hand(condition, value):
    """
    condition: '=|>|<'
    value:     0 <= integer <= 40
    returns number of hands 
    """
    total_hands = 0
    hcp_combo = hcp_combos(condition, value)
    for each in hcp_combo:
        # each = ('A0', 'K0', 'Q4', 'J4')
        noOfHighCards = int(each[0][1]) + int(each[1][1]) + int(each[2][1]) + int(each[3][1])
        temp =  C(int(each[0][1]),4) * C(int(each[1][1]),4) * C(int(each[2][1]),4) * C(int(each[3][1]),4) * C(13 - noOfHighCards, 36) 
        total_hands = total_hands + temp
    return total_hands

def hcp_range_hand(low, high):
    result = 0
    for each in range(low, high+1):
        result = result + hcp_hand('=', each)
    return result

# end this section for HCP calculations ***********************************


# this section for both HCP and distribution calculations *****************
def hcp_distr_hand(value, distr, condition='='):
    """
    condition: '='
    value:     0 <= integer <= 40
    distr:     '5-3-3-2'
    returns number of hands 
    """
    total_hands = 0
    hcp_combo = hcp_combos(condition, value) 
    result = 0
    for hcp in hcp_combo:
        # hcp = ('A1', 'K1', 'Q1', 'J1')
        aces = topHonorPermuSet(int(hcp[0][1]), 4)
        kings = topHonorPermuSet(int(hcp[1][1]), 4)
        queens = topHonorPermuSet(int(hcp[2][1]), 4)
        jacks = topHonorPermuSet(int(hcp[3][1]), 4)
        print (aces)
        print (kings)
        print (queens)
        print (jacks)
        print ('')

        specific_distr = getSpecficDistrs(distr)
        for dstr in specific_distr:
            # ('4', '3', '3', '3')
            dstr = map(lambda x: int(x), dstr) # should maybe do this in getSpecficDistrs(distr) function
#            if sum(aces) == 0:
#                pass # do nothing
#            else:
#                pass

#        kings = topHonorPermuSet(int(dstr[1][1]), 4)    
#        queens = topHonorPermuSet(int(dstr[2][1]), 4)    
#        jacks = topHonorPermuSet(int(dstr[3][1]), 4)    

def waysToPlaceHonor(n):
    if n == 0:
        return 0
    elif n == 1:
        return len(set(itertools.permutations([0,0,0,1]))) 
    elif n == 2:
        return len(set(itertools.permutations([0,0,1,1]))) 
    elif n == 3:
        return len(set(itertools.permutations([0,1,1,1]))) 
    elif n == 4:
        return len(set(itertools.permutations([1,1,1,1]))) 

def topHonorPermuSet(n, slots):
    if n > slots:
        print ('function topHonorPermuSet error, n > slots')
    if n == 0:
#        return [(0,0,0,0)]    
        return False
    if slots == 4:
        if n == 1:
            return list(set(itertools.permutations([0,0,0,1]))) 
        elif n == 2:
            return list(set(itertools.permutations([0,0,1,1]))) 
        elif n == 3:
            return list(set(itertools.permutations([0,1,1,1]))) 
        elif n == 4:
            return list(set(itertools.permutations([1,1,1,1]))) 
    elif slots == 3:
        if n == 1:
            return list(set(itertools.permutations([0,0,1]))) 
        elif n == 2:
            return list(set(itertools.permutations([0,1,1]))) 
        elif n == 3:
            return list(set(itertools.permutations([1,1,1]))) 
    elif slots == 2:
        if n == 1:
            return list(set(itertools.permutations([0,1]))) 
        elif n == 2:
            return list(set(itertools.permutations([1,1]))) 
    elif slots == 1:
        if n == 1:
            return list(set(itertools.permutations([1]))) 

def diff(x, y):
    # x: (3,4,5)
    # y: (1,1,1)
    # result: (3,4,5) - (1,1,1) = (2,3,4)
    return list(map(operator.sub, x, y))

def add(x,y):
    # x: (3,4,5)
    # y: (1,1,1)
    # result: (3,4,5) + (1,1,1) = (4,5,6)
    if len(x) != len(y):
        print ('function add error, len(x) <> len(y)')
        return False
    i = 0
    result = [0]*len(x)
    while i < len(x):
        result[i] = x[i] + y[i]
        i = i + 1
    return result

def addTuples(x):
    # x: ( (1, 0, 1, 0), (0, 0, 0, 1) )
    # returns (1, 0, 1, 0) + (0, 0, 0, 1) = (1,0,1,1)
    print (x[0])
    result = [0]*len(x[0])
    print (result)
    for each in x:
        result = add(result, each)
    return result
    
def negValInTpl(x):
    # x: tuple or list
    # returns True if any value is -ve (3,2,-1,0)
    for each in x:
        if each < 0:
            return True
    return False

def toC(highCards, lowCards):
    # highCards: ((1, 0, 1, 0), (0, 0, 0, 1))
    # lowCards: (3,3,2,2)
    # result: C(1,4)*C(0,0)*C(3,9) * C(0,0)*C(0,0)*C(3,9) * C(1,0)*C(0,0)*C(2,9) * C(0,4)*C(1,4)*C(2,9)
    print ('toC ************************')
    print (highCards)
    print (lowCards)
    slot_0 = C(lowCards[0],9) # X-3-3-3
    slot_1 = C(lowCards[1],9) # 4-X-3-3
    slot_2 = C(lowCards[2],9) # 4-3-X-3
    slot_3 = C(lowCards[3],9) # 4-3-3-X
    i = 0
    while i < len(highCards):
        slot_0 = slot_0 * C(highCards[i][0],4) 
        slot_1 = slot_1 * C(highCards[i][1],4) 
        slot_2 = slot_2 * C(highCards[i][2],4) 
        slot_3 = slot_3 * C(highCards[i][3],4) 
        i = i + 1
    print (slot_0 * slot_1 * slot_2 * slot_3/4)
    print ('end toC ********************')
    return slot_0 * slot_1 * slot_2 * slot_3/4
    
# end this section for both HCP and distribution calculations *************







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

GENERIC_DISTRIBUTIONS_HAND = ['4-3-3-3', '4-4-3-2', '5-3-3-2', '5-4-2-2', '4-4-4-1',
                              '5-4-3-1', '6-3-2-2', '6-3-3-1', '5-5-2-1', '6-4-2-1', '7-2-2-2',
                              '5-4-4-0', '7-3-2-1', '5-5-3-0', '6-5-1-1', '6-4-3-0', '7-4-1-1'
                              '6-5-2-0', '7-3-3-0', '8-2-2-1', '7-4-2-0', '8-3-1-1', '6-6-1-0',
                              '7-5-1-0', '8-3-2-0', '8-4-1-0', '9-2-1-1', '9-2-2-0', '7-6-0-0',
                              '9-3-1-0', '8-5-0-0', '10-1-1-1','9-4-0-0', '10-2-1-0','10-3-0-0',
                              '11-1-1-0','11-2-0-0','12-1-0-0','13-0-0-0']





GENERIC_DISTRIBUTIONS_TWO_HANDS = ['26-0-0-0', '25-1-0-0', '24-2-0-0', '24-1-1-0', '23-3-0-0', '23-2-1-0', '23-1-1-1', '22-4-0-0', '22-3-1-0', '22-2-2-0', '22-2-1-1', '21-5-0-0', '21-4-1-0', '21-3-2-0', '21-3-1-1', '21-2-2-1', '20-6-0-0', '20-5-1-0', '20-4-2-0', '20-4-1-1', '20-3-3-0', '20-3-2-1', '20-2-2-2', '19-7-0-0', '19-6-1-0', '19-5-2-0', '19-5-1-1', '19-4-3-0', '19-4-2-1', '19-3-3-1', '19-3-2-2', '18-8-0-0', '18-7-1-0', '18-6-2-0', '18-6-1-1', '18-5-3-0', '18-5-2-1', '18-4-4-0', '18-4-3-1', '18-4-2-2', '18-3-3-2', '17-9-0-0', '17-8-1-0', '17-7-2-0', '17-7-1-1', '17-6-3-0', '17-6-2-1', '17-5-4-0', '17-5-3-1', '17-5-2-2', '17-4-4-1', '17-4-3-2', '17-3-3-3', '16-10-0-0', '16-9-1-0', '16-8-2-0', '16-8-1-1', '16-7-3-0', '16-7-2-1', '16-6-4-0', '16-6-3-1', '16-6-2-2', '16-5-5-0', '16-5-4-1', '16-5-3-2', '16-4-4-2', '16-4-3-3', '15-11-0-0', '15-10-1-0', '15-9-2-0', '15-9-1-1', '15-8-3-0', '15-8-2-1', '15-7-4-0', '15-7-3-1', '15-7-2-2', '15-6-5-0', '15-6-4-1', '15-6-3-2', '15-5-5-1', '15-5-4-2', '15-5-3-3', '15-4-4-3', '14-12-0-0', '14-11-1-0', '14-10-2-0', '14-10-1-1', '14-9-3-0', '14-9-2-1', '14-8-4-0', '14-8-3-1', '14-8-2-2', '14-7-5-0', '14-7-4-1', '14-7-3-2', '14-6-6-0', '14-6-5-1', '14-6-4-2', '14-6-3-3', '14-5-5-2', '14-5-4-3', '14-4-4-4', '13-13-0-0', '13-12-1-0', '13-11-2-0', '13-11-1-1', '13-10-3-0', '13-10-2-1', '13-9-4-0', '13-9-3-1', '13-9-2-2', '13-8-5-0', '13-8-4-1', '13-8-3-2', '13-7-6-0', '13-7-5-1', '13-7-4-2', '13-7-3-3', '13-6-6-1', '13-6-5-2', '13-6-4-3', '13-5-5-3', '13-5-4-4', '12-12-2-0', '12-12-1-1', '12-11-3-0', '12-11-2-1', '12-10-4-0', '12-10-3-1', '12-10-2-2', '12-9-5-0', '12-9-4-1', '12-9-3-2', '12-8-6-0', '12-8-5-1', '12-8-4-2', '12-8-3-3', '12-7-7-0', '12-7-6-1', '12-7-5-2', '12-7-4-3', '12-6-6-2', '12-6-5-3', '12-6-4-4', '12-5-5-4', '11-11-4-0', '11-11-3-1', '11-11-2-2', '11-10-5-0', '11-10-4-1', '11-10-3-2', '11-9-6-0', '11-9-5-1', '11-9-4-2', '11-9-3-3', '11-8-7-0', '11-8-6-1', '11-8-5-2', '11-8-4-3', '11-7-7-1', '11-7-6-2', '11-7-5-3', '11-7-4-4', '11-6-6-3', '11-6-5-4', '11-5-5-5', '10-10-6-0', '10-10-5-1', '10-10-4-2', '10-10-3-3', '10-9-7-0', '10-9-6-1', '10-9-5-2', '10-9-4-3', '10-8-8-0', '10-8-7-1', '10-8-6-2', '10-8-5-3', '10-8-4-4', '10-7-7-2', '10-7-6-3', '10-7-5-4', '10-6-6-4', '10-6-5-5', '9-9-8-0', '9-9-7-1', '9-9-6-2', '9-9-5-3', '9-9-4-4', '9-8-8-1', '9-8-7-2', '9-8-6-3', '9-8-5-4', '9-7-7-3', '9-7-6-4', '9-7-5-5', '9-6-6-5', '8-8-8-2', '8-8-7-3', '8-8-6-4', '8-8-5-5', '8-7-7-4', '8-7-6-5', '8-6-6-6', '7-7-7-5', '7-7-6-6']

SUIT_COMBO = [('S', 'H', 'D', 'C'), ('S', 'H', 'C', 'D'), ('S', 'D', 'H', 'C'), ('S', 'D', 'C', 'H'), ('S', 'C', 'H', 'D'), ('S', 'C', 'D', 'H'), ('H', 'S', 'D', 'C'), ('H', 'S', 'C', 'D'), ('H', 'D', 'S', 'C'), ('H', 'D', 'C', 'S'), ('H', 'C', 'S', 'D'), ('H', 'C', 'D', 'S'), ('D', 'S', 'H', 'C'), ('D', 'S', 'C', 'H'), ('D', 'H', 'S', 'C'), ('D', 'H', 'C', 'S'), ('D', 'C', 'S', 'H'), ('D', 'C', 'H', 'S'), ('C', 'S', 'H', 'D'), ('C', 'S', 'D', 'H'), ('C', 'H', 'S', 'D'), ('C', 'H', 'D', 'S'), ('C', 'D', 'S', 'H'), ('C', 'D', 'H', 'S')]

# end CONSTANTS *******************************************************


# number of hands that can be dealt for first hand ********************************
r0 = SF(52,13)
#**********************************************************************************


# number of groups of hands that can dealt for first hand *************************
r1 = SF(52,13)/ A(13)
r1a = C(13,52)
# *********************************************************************************


# number of groups of hands that can be dealt with 4-3-3-3 specific distribution **
# 4-spades, 3-hearts, 3-diamonds, 3-clubs
r2 = (SF(13,4)/ A(4)) * (SF(13,3)/ A(3)) * (SF(13,3)/ A(3)) * (SF(13,3)/ A(3)) 
r2a = C(4,13) * C(3,13) * C(3,13) * C(3,13)
# *********************************************************************************

# number of groups of hands that can be dealt with 4-3-3-3 generic distribution****
r3 = set(list(itertools.permutations([4,3,3,3])))   # unique arrangements of 4-3-3-3 ie. 3-4-3-3, 4-3-3-3, 3-3-4-3, 3-3-3-4
r3a = len(r3)                                       # number of arrangements
r3b = C(4,13) * C(3,13) * C(3,13) * C(3,13)         # specific arrangement
r3c = r3a * r3b                                     # number of arrangement x specific arrangement
r3d = genericDistr_hands('4-3-3-3')


# *********************************************************************************

# number of groups of hands that can be dealt with 12 HCP *************************
r4 = hcp_hand('=',12)
# *********************************************************************************

# number of groups of hands that can be dealt with between 6 and 12 HCP ***********
# Ans = 375,974,133,568
r5 =  hcp_hand('=',6) + hcp_hand('=',7) + hcp_hand('=',8) + hcp_hand('=',9) \
      + hcp_hand('=',10) + hcp_hand('=',11) + hcp_hand('=',12)
r5a = hcp_range_hand(6,12)
# *********************************************************************************

# get specific distributions from a generic distribution **************************
r6 = getSpecficDistrs('5-3-3-2')
r6a = getSpecficDistrsCount('5-3-3-2')

# *********************************************************************************

# number of groups of hands with 1 hcp and 4-3-3-3 distribution ******************

r7 = C(3,9) * C(3,9) * C(3,9) * C(3,9) * C(1, 4)
r7a = C(4,9) * C(2,9) * C(3,9) * C(3,9) * C(1, 4)
r7b = r7 + 3*r7a

r7c = hcp_distr_hand(10, '4-3-3-3', condition='=')
# *********************************************************************************


# test stuff ********************



hcp_combo = hcp_combos('=', 2)
print ('each in hcp_combo')
for hcp in hcp_combo:
    print (' start **************************************')
    print (hcp)
    aces = topHonorPermuSet(int(hcp[0][1]), 4)
    kings = topHonorPermuSet(int(hcp[1][1]), 4)
    queens = topHonorPermuSet(int(hcp[2][1]), 4)
    jacks = topHonorPermuSet(int(hcp[3][1]), 4)
    tmp = []
    print ('aces')
    if aces:
        print (aces)
        tmp.append(aces)
    print ('kings')
    if kings:
        print (kings)
        tmp.append(kings)
    print ('queens')
    if queens:
        print (queens)
        tmp.append(queens)
    print ('jacks')
    if jacks:
        print (jacks)
        tmp.append(jacks)

    if len(tmp)==0:
        pass
    elif len(tmp)==1:    
        prod = itertools.product(tmp[0])
    elif len(tmp)==2:    
        prod = itertools.product(tmp[0], tmp[1])
    elif len(tmp)==3:    
        prod = itertools.product(tmp[0], tmp[1], tmp[2])
    elif len(tmp)==4:    
        prod = itertools.product(tmp[0], tmp[1], tmp[2], tmp[3])

    temp_ans = 0
    distr = [4,3,3,3]
    print ('item in prod')
    for item in prod:
        print (item)
        slots = distr
        slots = diff(slots, addTuples(item))
        if negValInTpl(slots):
            print ('negValInTpl(slots)')
        else:
            print (slots)
            print ('**slots**')
            temp_ans = temp_ans + toC(item, slots)
            final_answer = temp_ans * getSpecficDistrsCount('4-3-3-3')

    print ('final_answer: ' + cin(final_answer))
    print (' end ***************************************')
    




# end test stuff ****************
