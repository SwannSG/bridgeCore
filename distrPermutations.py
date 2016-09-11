"""
    Given a set of constraints
   
       nSmin, nSmax   nHmin, nHmax   nDmin, nDmax   nCmin, nCmax    

       nSmin + nHmin + nDmin + nCmin <= 13

    Compute distribution solutions in form

       nS-nH-nD-nC

    Answer given in result   
"""

import itertools

def genPosValues(low, high):
    # generate possible values
    l = []
    i = low
    while i <= high:
        l.append(i)
        i = i + 1
    return l
    

def setOrder(tpl, suitOrder):
    # set order to S-H-D-C
    suitOrder = list(suitOrder)
    result= str(tpl[suitOrder.index('S')]) + '-' + \
            str(tpl[suitOrder.index('H')]) + '-' + \
            str(tpl[suitOrder.index('D')]) + '-' + \
            str(tpl[suitOrder.index('C')])

    return result

def genericDistr(dataList):
    # distr with no suit order
    # from highest to lowest
    genericResult = set()
    for each in dataList:
        temp = each.split('-')
        temp.sort(reverse=True)
        genericResult.add(temp[0]+'-'+temp[1]+'-'+temp[2]+'-'+temp[3])
    return genericResult








SUIT_COMBO = [('S', 'H', 'D', 'C'), ('S', 'H', 'C', 'D'), ('S', 'D', 'H', 'C'), ('S', 'D', 'C', 'H'), ('S', 'C', 'H', 'D'), ('S', 'C', 'D', 'H'), ('H', 'S', 'D', 'C'), ('H', 'S', 'C', 'D'), ('H', 'D', 'S', 'C'), ('H', 'D', 'C', 'S'), ('H', 'C', 'S', 'D'), ('H', 'C', 'D', 'S'), ('D', 'S', 'H', 'C'), ('D', 'S', 'C', 'H'), ('D', 'H', 'S', 'C'), ('D', 'H', 'C', 'S'), ('D', 'C', 'S', 'H'), ('D', 'C', 'H', 'S'), ('C', 'S', 'H', 'D'), ('C', 'S', 'D', 'H'), ('C', 'H', 'S', 'D'), ('C', 'H', 'D', 'S'), ('C', 'D', 'S', 'H'), ('C', 'D', 'H', 'S')]



nlS = 0
nhS = 13

nlH = 0
nhH = 13

nlD = 0
nhD = 13

nlC = 0
nhC = 13

if nlS + nlH + nlD + nlC > 13:
    print ('error, exceeds 13')

values = {}
values['S'] = genPosValues(nlS, nhS)
values['H'] = genPosValues(nlH, nhH)
values['D'] = genPosValues(nlD, nhD)
values['C'] = genPosValues(nlC, nhC)

result = set()
for index, suitCombo in enumerate(SUIT_COMBO):
    # compute cartesian product
    for r in itertools.product(values[suitCombo[0]], values[suitCombo[1]], values[suitCombo[2]], values[suitCombo[3]]):
        if r[0] + r[1] + r[2] + r[3] == 13:
            # change order to S-H-D-C
            result.add(setOrder(r, suitCombo))

genericResult = genericDistr(result)
