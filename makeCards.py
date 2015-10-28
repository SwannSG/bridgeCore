__author__ = 'swannsg'

# clubs       1 - 13
# diamonds   14 - 26
# hearts     27 - 39
# spades     40 - 52

# 11 Jack
# 12 Queen
# 13 King
# 14 Ace

import random

honors = {11:'J', 12:'Q', 13:'K', 14:'A'}
honors_rev = {'J':11, 'Q':12, 'K':13, 'A':14}
aces = [13,26,39,52]
kings = [12,25,38,51]
queens = [11,24,37,50]
jacks = [10,23,36,49]
clubHonors = [10,11,12,13]
diamondHonors = [23,24,25,2,6]
heartHonors = [36,37,38,39]
spadeHonors = [49,50,51,52]

honorPoints = {'A':4, 'K':3, 'Q':2, 'J':1}

def deal():
    """
    randomly generate 4 hands
    """
    _range = range(1, 53)
    r = random.sample(_range, 52)
    return  (r[0:13], r[13:26], r[26:39], r[39:52])

def symbolToCard(x):
    """
        pass string symbol eg. AC, 2S
        return integer value
    """
    global honors_rev
    suit = x[-1]
    face = x[:-1]
    if not face.isdigit():
        face = honors_rev[face]
    else:
        face = int(face)
    if suit == 'C':
        return face - 1
    elif suit == 'D':
        return face + 12
    elif suit == 'H':
        return face + 25
    elif suit == 'S':
        return face + 38

def cardSymbol(x):
    """
        pass integer [2 ... 14]
        return symbol eg. 2 .... 10, J, Q, K, A
    """
    global honors
    if x <= 10:
        return x
    else:
        return honors[x]


def cardToSymbol(x):
    """
        pass integer representation of card
        return string representation eg 2C = 2 Clubs
    """
    if each >= 1 and each <= 13:
        # clubs
        x = x + 1
        return '%s%s' % (cardSymbol(x), 'C')
    elif each >= 14 and each <= 26:
        # diamonds
        x = x - 12
        return '%s%s' % (cardSymbol(x), 'D')
    elif each >= 27 and each <= 39:
        # hearts
        x = x - 25
        return '%s%s' % (cardSymbol(x), 'H')
    elif each >= 40 and each <= 52:
        # spades
        x = x - 38
        return '%s%s' % (cardSymbol(x), 'S')


class Suit:


    def __init__(self, suit, honors, whichSuit):
        self.length = len(suit)
        self.__offset = self.__offset(whichSuit)
        self.nHonors = self.__nHonors(suit, honors)
        self.vHonors = self.__vHonors(suit, honors)
        self.symbols = self.__symbols(suit)
        self.honors = self.__honors(self.symbols)
        self.nonhonors = self.__nonhonors(self.symbols)
        # number of exposed honors
        self.nexpHonors = self.__exposedHonors(self.honors) 
        # number of exposed honor points
        self.expHonorsPoints = self.__expHonorsPoints()
        self.suitValue = self.__suitValue()

    def __suitValue(self):
        return self.length + self.vHonors - self.expHonorsPoints
                  
    def __expHonorsPoints(self):
        nexp = self.nexpHonors - len(self.nonhonors) 
        if nexp > 0:
            expFaces = self.honors[-nexp:]
        else:
            expFaces = []
        n = 0
        global honorPoints 
        for  each in expFaces:
            n = n + honorPoints[each]
        return n
            

    def __nonhonors(self, symbols):
        l = []
        for each in symbols:
            if each in [2,3,4,5,6,7,8,9,10]:
                l.append(each)
        return l
        
    def __countHonor(self, honor, honors):
        if honor in honors:
            return 1
        else:
            return 0

    def __exposedHonors(self, honors):
        n = 0
        for each in honors:
            if each == 'J':
                r = 3 - self.__countHonor('A', honors) - self.__countHonor('K', honors) - self.__countHonor('Q', honors)
                r = 0 if r < 0 else r
                n = n + r
            elif each == 'Q':
                r = 2  - self.__countHonor('A', honors) - self.__countHonor('K', honors) - self.__countHonor('J', honors)
                r = 0 if r < 0 else r
                n = n + r
            elif each == 'K':
                r = 1  - self.__countHonor('A', honors) - self.__countHonor('Q', honors) - self.__countHonor('J', honors)
                r = 0 if r < 0 else r
                n = n + r
        return n    

    def __honors(self, symbols):
        l = []
        for each in symbols:
            if each in ['A', 'K', 'Q', 'J']:
                l.append(each)
        return l
    
    def __offset(self, whichSuit):
        if whichSuit == 'C':
            offset = -1
        elif whichSuit == 'D':
            offset = 12
        elif whichSuit == 'H':
            offset = 25
        elif whichSuit == 'S':
            offset = 38
        return offset


    def __nHonors(self, suit, honors):
        """
            return number of honors
        """
        n = 0
        for each in suit:
            if each in honors:
                n = n + 1    
        return n

    def __vHonors(self, suit, honors):
        """
            return value of honors
        """
        p = 0
        for each in suit:
            if each in honors:
                c = cardSymbol(each - self.__offset) 
                if c == 'A':
                    p = p + 4
                elif c == 'K':
                    p = p + 3
                elif c == 'Q':
                    p = p + 2
                elif c == 'J':
                    p = p + 1
        return p

    def __symbols(self, suit):
        """
            return symbol representaion of integers
        """
        l = []
        for each in suit:
            l.append(cardSymbol(each - self.__offset))
        return l

    def __repr__(self):
        """
            string representation of object
        """
        s = ''
        s = s + 'length: %s\n' % self.length
        s = s + 'nHonors: %s\n' % self.nHonors
        s = s + 'vHonors: %s\n' % self.vHonors
        s = s + 'symbols: %s\n' % self.symbols
        s = s + 'honors: %s\n' % self.honors
        s = s + 'nexpHonors: %s\n' % self.nexpHonors
        s = s + 'nexpHonorPoints: %s\n' % self.expHonorsPoints
        s = s + 'suitValue: %s\n' % self.suitValue
        return s


class analyseHand:

    def __init__(self, hand):
        self.hand = hand
        self.clubs = self.__clubs(self.hand)
        self.clubDetails = Suit(self.clubs, clubHonors, 'C')
        self.diamonds = self.__diamonds(self.hand)
        self.diamondDetails = Suit(self.diamonds, diamondHonors, 'D') 
        self.hearts = self.__hearts(self.hand)
        self.heartDetails = Suit(self.hearts, heartHonors, 'H')
        self.spades = self.__spades(self.hand)
        self.spadeDetails = Suit(self.spades, spadeHonors, 'S')
        # distribution C-D-H-S
        self.distr = '%s-%s-%s-%s' % (len(self.clubs),
                                      len(self.diamonds),
                                      len(self.hearts),
                                      len(self.spades))
        # number of
        self.aces = self.__aces(self.hand)
        self.kings = self.__kings(self.hand)
        self.queens = self.__queens(self.hand)
        self.jacks = self.__jacks(self.hand)
        # high card points                              
        self.HCP = self.aces*4 + self.kings*3 + self.queens*2 + self.jacks
        # long points
        self.LP = self.__LP()
        # short points
        self.SP = self.__SP()
        # Swann points
        self.Swann = self.clubDetails.suitValue + self.diamondDetails.suitValue + self.heartDetails.suitValue + self.spadeDetails.suitValue 
        self.SwannSuit = '%s-%s-%s-%s' % (self.clubDetails.suitValue, self.diamondDetails.suitValue, self.heartDetails.suitValue, self.spadeDetails.suitValue) 
        

    def __repr__(self):
        """
            string representation of object
        """
        s = ''
        s = s + 'distribution: %s\n' % self.distr
        s = s + 'SwannSuitP: %s\n' % self.SwannSuit
        s = s + 'HCP: %s\n' % self.HCP
        s = s + 'LP: %s\n' % self.LP
        s = s + 'SP: %s\n' % self.SP
        s = s + 'SwannPoints: %s\n' % self.Swann
        s = s + 'Clubs: %s\n' % self.clubDetails.symbols
        s = s + 'Diamonds: %s\n' % self.diamondDetails.symbols
        s = s + 'Hearts: %s\n' % self.heartDetails.symbols
        s = s + 'Spades: %s\n' % self.spadeDetails.symbols
        return s

    def __LP(self):
        """
            long points
        """
        p = 0
        for each in self.distr.split('-'):
            each = int(each)
            if (each - 4) > 0:
                p = p + (each - 4)
        p = p + self.HCP
        return p

    def __SP(self):
        """
            short points
        """
        p = 0
        for each in self.distr.split('-'):
            each = int(each)
            if each == 0:
                p = p + 3
            elif each == 1:
                p = p + 2
            elif each == 2:
                p = p + 1
        p = p + self.HCP
        return p
        
    def __aces(self, hand):
        global aces
        n = 0                              
        for each in hand:
            if each in aces:                               
                n = n + 1
        return n

    def __kings(self, hand):
        global kings
        n = 0                              
        for each in hand:
            if each in kings:                               
                n = n + 1
        return n

    def __queens(self, hand):
        global queens
        n = 0                              
        for each in hand:
            if each in queens:                               
                n = n + 1
        return n

    def __jacks(self, hand):
        global jacks
        n = 0                              
        for each in hand:
            if each in jacks:                              
                n = n + 1
        return n

    def __clubs(self, hand):
        l = []
        for each in hand:
            if each <= 13:
                l.append(each)
        l.sort(reverse=True)
        return l
    
    def __diamonds(self, hand):
        l = []
        for each in hand:
            if each >= 14 and each <= 26:
                l.append(each)
        l.sort(reverse=True)
        return l

    def __hearts(self, hand):
        l = []
        for each in hand:
            if each >= 27 and each <= 39:
                l.append(each)
        l.sort(reverse=True)
        return l

    def __spades(self, hand):
        l = []
        for each in hand:
            if each >= 40 and each <= 52:
                l.append(each)
        l.sort(reverse=True)
        return l

def openBid(e):
    if e.LP >= 23:
        return '2C'

    if e.LP >= 13 and len(e.hearts) >= 5:
        return '1H'

    if e.LP >= 13 and len(e.spades) >= 5:
        return '1S'

    if e.LP >= 13 and e.LP <= 15:
        return '1D'
    
    if e.LP >= 16 and e.LP <= 19:
        return '1C'

    if e.SP >= 6 and len(e.clubs) >= 7:
        return '3C' 

    if e.SP >= 6 and len(e.diamonds) >= 6:
        if len(e.diamonds) == 6:
            return '2D'
        elif len(e.diamonds) == 7:
            return '3D'
        else:
            return '4D'

    if e.SP >= 6 and len(e.hearts) >= 6:
        if len(e.hearts) == 6:
            return '2H'
        elif len(e.hearts) == 7:
            return '3H'
        else:
            return '4H'

    if e.SP >= 6 and len(e.spades) >= 6:
        if len(e.spades) == 6:
            return '2S'
        elif len(e.spades) == 7:
            return '3S'
        else:
            return '4S'

    return 'Pass'




north, south, east, west = deal()

N = analyseHand(north)
S = analyseHand(south)
E = analyseHand(east)
W = analyseHand(west)

print 'NORTH'
print N
print '\nSOUTH'
print S
print '\nEAST'
print E
print '\nWEST'
print W

# bidding sequence
print 'N: %s' % openBid(N)
print 'E: %s' % openBid(E)
print 'S: %s' % openBid(S)
print 'W: %s' % openBid(W)
