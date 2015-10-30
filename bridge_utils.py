from bridge_config import *

def symToInt(symbol):
    global SYM_TO_INT
    return SYM_TO_INT[symbol]

def intToSym(integer):
    global INT_TO_SYM
    return INT_TO_SYM[integer]

def getSymbols(cards, ordered=True):
    """
        return list of symbols
    """
    l = []
    if ordered:
        split_by_suit = split_into_suits(cards)
        for each in split_by_suit:
            each.sort(reverse=True)
            l = l + each            
    symbols = []
    for each in l:
        symbols.append(intToSym(each))
    return symbols


def count_of_cards(cards, what_cards):
    """
        returns number of what_cards in cards
        cards:      sequence of cards as integers
        what_cards: sequence of what_cards as integers

        can be used to count aces, kings, queens, jacks etc.
    """
    return len(set.intersection(set(cards), set(what_cards)))

def split_into_suits(cards):
    """
        split hand of cards into suits
        return (club_list, diamond_list, heart_list, spade_list)
    """
    return ([x for x in cards if x <= 13],               #clubs
            [x for x in cards if (x >= 14 and x <= 26)], #diamonds
            [x for x in cards if (x >= 27 and x <= 39)], #hearts
            [x for x in cards if x >= 40])               #spades

def summary_of_distribution(cards):
    """
        split hand of cards into summarised distribution 
        return (no_of_clubs, no_of_diamonds, no_of_hearts, no_of_spades)
    """
    split = split_into_suits(cards)
    return (len(split[0]), len(split[1]),len(split[2]), len(split[3]))


def deal_distribution(deal):
    """
        deal: tuple([hand_0], [hand_1], [hand_2], [hand_3])
        return: ((nC, nD, nH, nS), (nC, nD, nH, nS), (nC, nD, nH, nS), (nC, nD, nH, nS)) 
    """
    l = []
    for hand in deal:
        l.append(summary_of_distribution(hand))
    return tuple(l)

def deal_hcp_distr(deal):
    """
        deal: tuple([hand_0], [hand_1], [hand_2], [hand_3])
        return: ((hcp_C, hcp_D, hcp_H, hcp_S), (hcp_C, hcp_D, hcp_H, hcp_S), (hcp_C, hcp_D, hcp_H, hcp_S), (hcp_C, hcp_D, hcp_H, hcp_S)) 
    """
    l = []
    for hand in deal:
        l.append(hcp_distr(hand))
    return tuple(l)

    

def hcp_per_suit(split):
    """
        HCP per suit
        return (hcp_clubs, hcp_diamonds, hcp_hearts, hcp_spades)
        split: ([clubs], [diamonds], [hearts], [spades])
            where [clubs]: list of integer values
    """
    hcp_split = []
    for each_suit in split:
        hcp_split.append(hcp_for_cards(each_suit))
    return tuple(hcp_split)


def hcp_distr(cards):
    """
        return hcp per suit for a set of cards
        (hcp_C, hcp_D, hcp_H, hcp_S)
    """
    return hcp_per_suit(split_into_suits(cards))


def hcp_for_cards(cards):
    """
        return high card points for a set of cards as single integer
    """
    hcp = 0
    hcp = hcp + count_of_cards(cards, ACES)*HCP['ACE']
    hcp = hcp + count_of_cards(cards, KINGS)*HCP['KING']
    hcp = hcp + count_of_cards(cards, QUEENS)*HCP['QUEEN']
    hcp = hcp + count_of_cards(cards, JACKS)*HCP['JACK']
    return hcp

        
def deal_hcp(deal):
    """
        deal: tuple([hand_0], [hand_1], [hand_2], [hand_3])
        return: (hcp_1, hcp_2, hcp_3, hcp_4)
    """
    l = []
    for hand in deal:
        l.append(hcp_for_cards(hand))
    return tuple(l)
        
class Hand:

    def __init__(self, hand):
        """
            hand: [hand] of integers, length 13
        """
        self.hand = hand
        self.symbols = getSymbols(hand)
        self.distr = summary_of_distribution(hand)
        self.hcp_distr = hcp_distr(hand)
        self.hcp = hcp_for_cards(hand)

    def __repr__(self):
        #hcp, hcp_distr, distr
        return '%s\n%s\t\t%s\t\t%s' % (str(self.symbols), self.hcp, str(self.hcp_distr), str(self.distr))

class Partnership:

    def __init__(self, hand_1, hand_2):
        self.hand_1 = Hand(hand_1)
        self.hand_2 = Hand(hand_2)
        self.hcp = self.hand_1.hcp + self.hand_2.hcp
        self.distr = tuple([sum(x) for x in zip(self.hand_1.distr, self.hand_2.distr)])
        self.hcp_distr = tuple([sum(x) for x in zip(self.hand_1.hcp_distr, self.hand_2.hcp_distr)])

    def __repr__(self):
        return '%s\t\t%s\t\t%s' % (self.hcp, str(self.hcp_distr), str(self.distr)) 

