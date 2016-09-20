# generate and classify random hands

import random

def getSuitCount(suit, hand):
    result = 0
    for each in hand:
        if each[1]==suit:
            result = result + 1
    return result


def getActualDistribution(hand):
    return str(getSuitCount('s',hand)) + '-' +  \
           str(getSuitCount('h',hand)) + '-' +  \
           str(getSuitCount('d',hand)) + '-' +  \
           str(getSuitCount('c',hand))

def getGenericDistribution(actual_distr):
    pass
    

PACK = ['2c01', '3c02', '4c03', '5c04', '6c05', '7c06', '8c07', '9c08', 'tc09',
  'jc10', 'qc11', 'kc12', 'ac13', '2d14', '3d15', '4d16', '5d17', '6d18',
  '7d19', '8d20', '9d21', 'td22', 'jd23', 'qd24', 'kd25', 'ad26', '2h27',
  '3h28', '4h29', '5h30', '6h31', '7h32', '8h33', '9h34', 'th35', 'jh36',
  'qh37', 'kh38', 'ah39', '2s40', '3s41', '4s42', '5s43', '6s44', '7s45',
  '8s46', '9s47', 'ts48', 'js49', 'qs50', 'ks51', 'as52']

# generate
pack = PACK
random.shuffle(pack)
h1 = pack[:13]
h2 = pack[14:27]
h3 = pack[28:41]
h4 = pack[42:]






# classify
# #itterations         (n)  
# generic distribution (gd)
# actual distribution  (ad)
# point count          (pc) 
