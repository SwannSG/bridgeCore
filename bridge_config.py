SYM_TO_INT =  {
      '2C':1, '3C':2, '4C':3, '5C':4, '6C':5, '7C':6, '8C':7, '9C':8, 'TC':9, 'JC':10, 'QC':11, 'KC':12, 'AC':13,
      '2D':14, '3D':15, '4D':16, '5D':17, '6D':18, '7D':19, '8D':20, '9D':21, 'TD':22, 'JD':23, 'QD':24, 'KD':25, 'AD':26,
      '2H':27, '3H':28, '4H':29, '5H':30, '6H':31, '7H':32, '8H':33, '9H':34, 'TH':35, 'JH':36, 'QH':37, 'KH':38, 'AH':39,
      '2S':40, '3S':41, '4S':42, '5S':43, '6S':44, '7S':45, '8S':46, '9S':47, 'TS':48, 'JS':49, 'QS':50, 'KS':51, 'AS':52
      }


INT_TO_SYM =  {
      1:'2C', 2:'3C', 3:'4C', 4:'5C', 5:'6C', 6:'7C', 7:'8C', 8:'9C', 9:'TC', 10:'JC', 11:'QC', 12:'KC', 13:'AC',
      14:'2D', 15:'3D', 16:'4D', 17:'5D', 18:'6D', 19:'7D', 20:'8D', 21:'9D', 22:'TD', 23:'JD', 24:'QD', 25:'KD', 26:'AD',
      27:'2H', 28:'3H', 29:'4H', 30:'5H', 31:'6H', 32:'7H', 33:'8H', 34:'9H', 35:'TH', 36:'JH', 37:'QH', 38:'KH', 39:'AH',
      40:'2S', 41:'3S', 42:'4S', 43:'5S', 44:'6S', 45:'7S', 46:'8S', 47:'9S', 48:'TS', 49:'JS', 50:'QS', 51:'KS', 52:'AS'
      }

ACES = (13, 26, 39, 52)
KINGS = (12, 25, 38, 51)
QUEENS = (11, 24, 37, 50)
JACKS = (10, 23, 36, 49)
TENS = (9, 22, 35, 48)

HCP = {'ACE':4, 'KING': 3, 'QUEEN': 2, 'JACK': 1} 

CLUBS =    [1,2,3,4,5,6,7,8,9,10,11,12,13]
DIAMONDS = [14,15,16,17,18,19,20,21,22,22,24,25,26]
HEARTS =   [27,28,29,30,31,32,33,34,35,36,37,38,39]
SPADES =   [40,41,42,43,44,45,46,47,48,49,50,51,52]    

MAX_ITERATIONS = 1000000


class Hand:
    """
    Hand
        13 cards that are initially dealt

    Hand properties
        cards: unsorted integer representation of cards in hand
        sorted_cards: sorted integer representation of cards in hand
    """
    def __init__(self, cards):
        """
            cards: unsorted integer representation of cards in hand
                  length 13
        """
        if len(cards) <> 13:
            print 'error: raw_hand length <> 13'
            return False
        self.cards = cards
        self.clubs = self.get_clubs(self.cards)
        self.diamonds = self.get_diamonds(self.cards)
        self.hearts = self.get_hearts(self.cards) 
        self.spades = self.get_spades(self.cards)
        self.clubs_hcp = self.get_hcp(self.clubs)
        self.diamonds_hcp = self.get_hcp(self.diamonds)
        self.hearts_hcp = self.get_hcp(self.hearts)
        self.spades_hcp = self.get_hcp(self.spades)
        self.hcp_per_suit = [self.clubs_hcp, self.diamonds_hcp, self.hearts_hcp, self.spades_hcp]
        self.hcp_total = self.clubs_hcp + self.diamonds_hcp + self.hearts_hcp + self.spades_hcp
        self.honours = self.get_honours(self.cards)
        self.clubs_ltc = self.losing_trick_count(self.clubs)
        self.diamonds_ltc = self.losing_trick_count(self.diamonds)
        self.hearts_ltc = self.losing_trick_count(self.hearts)
        self.spades_ltc = self.losing_trick_count(self.spades)
        self.ltc_per_suit = [self.clubs_ltc, self.diamonds_ltc, self.hearts_ltc, self.spades_ltc]
        self.ltc_total = self.clubs_ltc + self.diamonds_ltc + self.hearts_ltc + self.spades_ltc
        self.sorted_cards = self.clubs + self.diamonds + self.hearts + self.spades
        self.nclubs = len(self.clubs)
        self.ndiamonds = len(self.diamonds)
        self.nhearts = len(self.hearts)
        self.nspades = len(self.spades)
        self.distribution = [self.nclubs, self.ndiamonds, self.nhearts, self.nspades]


    def get_hcp(self, cards):
        """
            pass list of cards as integers
            returns total high card points
        """
        hcp = 0
        ntens, njacks, nqueens, nkings, naces = self.get_honours(cards) 
        hcp = naces*HCP['ACE'] + nkings*HCP['KING'] + nqueens*HCP['QUEEN'] + njacks*HCP['JACK']  
        return hcp

    def get_honours(self, cards):
        """
            pass list of cards as integers
            return [number of tens, jacks, queens, kings, aces] 
        """
        set_cards = set(cards)
        naces = len(set.intersection(set_cards, set(ACES)))
        nkings = len(set.intersection(set_cards, set(KINGS)))
        nqueens = len(set.intersection(set_cards, set(QUEENS)))
        njacks = len(set.intersection(set_cards, set(JACKS)))
        ntens = len(set.intersection(set_cards, set(TENS)))
        return [ntens, njacks, nqueens, nkings, naces]        

    def get_clubs(self, cards):
        """
            pass list of cards as integers
            returns sorted clubs list
        """
        result = [x for x in cards if x <= 13]
        result.sort(reverse=True)
        return result

    def get_diamonds(self, cards):
        """
            pass list of cards as integers
            returns sorted diamonds list
        """
        result = [x for x in cards if (x >= 14 and x <= 26)]
        result.sort(reverse=True)
        return result

    def get_hearts(self, cards):
        """
            pass list of cards as integers
            returns sorted hearts list
        """
        result = [x for x in cards if (x >= 27 and x <= 39)]
        result.sort(reverse=True)
        return result

    def get_spades(self, cards):
        """
            pass list of cards as integers
            returns sorted spades list
        """
        result = [x for x in cards if  x >=40]
        result.sort(reverse=True)
        return result

    def losing_trick_count(self, suit):
        """
            pass suit of cards as integers
            returns losing trick count for suit
        """
        ntens, njacks, nqueens, nkings, naces = self.get_honours(suit)
        if naces == 1 and nkings == 1 and nqueens == 1:
            nlosers = 0
        elif naces == 1 and nkings == 1:
            nlosers = 1
        elif naces == 1 and nqueens == 1:
            nlosers = 1.5
        elif naces == 1:
            nlosers = 2
        elif nkings == 1:
            nlosers = 2
        else:
            if len(suit) >= 3:
                nlosers = 3
            else:
                nlosers = len(suit)
        return nlosers
        

    def symbols(self, cards):
        """
            pass list of cards as integers
            returns list of cards as character representaion
        """
        result = []
        for each in cards:
            result.append(INT_TO_SYM[each])
        return result

    def select_hand_hcp(self, bounds):
        """
            pass bounds [lb(lower bound), ub (upper bound)]
            returns true if band met
        """
        lb = bounds[0]
        ub = bounds[1]
        if self.hcp_total >= lb and self.hcp_total <= ub:
            return True
        return False

    def select_hand_ltc(self, bounds):
        """
            pass lb(lower bound) and ub (upper bound)
            returns true if band met
        """
        lb = bounds[0]
        ub = bounds[1]
        if self.ltc_total >= lb and self.ltc_total <= ub:
            return True
        return False

    def select_hand_distribution(self, distr):
        """
            pass distribution list [nC, nD, nH, nS]
            return True if distribution met
        """
        if self.distribution == distr:
            return True
        return False


    def __repr__(self):
        result = []
        result.append('HCP: %s' % self.hcp_total)
        result.append(self.hcp_per_suit)
        #result.append('')
        result.append('Distribution [C, D, H, S]' )
        result.append(self.distribution)
        #result.append('')
        result.append('Honours [tens, jacks, queens, kings, aces]' )
        result.append(self.honours)
        #result.append('')
        result.append('Losing Trick Count [C, D, H, S]: %s' % self.ltc_total)
        result.append(self.ltc_per_suit)
        result.append('Hand')
        result.append(self.symbols(self.sorted_cards))
        #result.append('')
        output = ''
        for each in result:
            output = '%s\n%s' % (output, str(each))
        return output

class Partnership:

    def __init__(self, hand, partner_hand):
        """
            hand, parner_hand are objects derived from Hand
        """
        self.hand = hand
        self.partner_hand = partner_hand
        self.p_hcp_total = hand.hcp_total + partner_hand.hcp_total
        self.p_distr = [hand.distribution[0] + partner_hand.distribution[0], 
                        hand.distribution[1] + partner_hand.distribution[1],
                        hand.distribution[2] + partner_hand.distribution[2],
                        hand.distribution[3] + partner_hand.distribution[3]]

    def select_partnership_hcp(self, bounds):
        """
            pass bounds [lb(lower bound), ub (upper bound)]
            returns true if band met
        """
        lb = bounds[0]
        ub = bounds[1]
        if self.p_hcp_total >= lb and self.p_hcp_total <= ub:
            return True
        return False

    def select_partnership_distribution(self, partnership_distr):
        """
            pass distribution list [nC, nD, nH, nS]
            return True if distribution met
        """
        if self.p_distr == partnership_distr:
            return True
        return False

    def __repr__(self):
        result = list()
        result.append('Partnership **************')
        result.append('hcp: %s' % self.p_hcp_total)
        result.append('distr: %s' % self.p_distr)
        result.append('Hand 1 *******************')
        result.append(self.hand)
        result.append('Hand 2 *******************')
        result.append(self.partner_hand)
        result.append('')
        output = ''
        for each in result:
            output = '%s\n%s' % (output, str(each))
        return output

def deal_cards():
    """
    randomly generate 4 hands
    """
    import random
    _range = range(1, 53)
    r = random.sample(_range, 52)
    return  (r[0:13], r[13:26], r[26:39], r[39:52])

class HandSelection:

    def __init__(self, selection_criteria='none', hcp_criteria=[13,15], ltc_criteria=[7,8], distr_criteria=[3,3,3,4]):
        """
            selection_criteria: 'hcp' or 'ltc' or 'distr' or 'hcp_distr' or 'none'
        """
        self.deal = ''
        self.selection_criteria = selection_criteria
        self.hcp_criteria = hcp_criteria
        self.ltc_criteria = ltc_criteria
        self.distr_criteria = distr_criteria
        self.index = -1     # not found
        self.solution_found = False
        self.count = 0      # number of itterations
        if self.selection_criteria == 'none':
            # no selection criteria
            self.none_selection()
        elif self.selection_criteria == 'hcp':
            self.hcp_selection(self.hcp_criteria)
        elif self.selection_criteria == 'ltc':
            self.ltc_selection(self.ltc_criteria)
        elif self.selection_criteria == 'hcp_distr':
            self.hcp_distr_selection(self.hcp_criteria, self.distr_criteria)
        self.teams = [('',''), ('','')]


    def none_selection(self):
        deal = deal_cards()
        self.deal = deal
        self.index = 0
        self.solution_found = True
        self.count = 1
        self.teams = [(0,1), (2,3)]

    def hcp_selection(self, hcp_criteria):
        found = False
        i = 1
        while i <= MAX_ITERATIONS:
            deal = deal_cards()
            for index, item in enumerate(deal):
                hand = Hand(item)
                if hand.select_hand_hcp(hcp_criteria):
                    found = True
                    self.index = index
                    break
            if found:
                self.solution_found = True
                self.deal = deal
                self.teams = __get_teams(self.index)
                # [(self.index,1), (2,3)]
                break
            i = i + 1
        self.count = i

    def ltc_selection(self, ltc_criteria):
        found = False
        i = 1
        while i <= MAX_ITERATIONS:
            deal = deal_cards()
            for index, item in enumerate(deal):
                hand = Hand(item)
                if hand.select_hand_ltc(hcp_criteria):
                    found = True
                    self.index = index
                    break
            if found:
                self.solution_found = True
                self.deal = deal
                break
            i = i + 1
        self.count = i

    def hcp_distr_selection(self, hcp_criteria, distr_criteria):
        found = False
        i = 1
        while i <= MAX_ITERATIONS:
            deal = deal_cards()
            for index, item in enumerate(deal):
                hand = Hand(item)
                if hand.select_hand_hcp(hcp_criteria) and hand.select_hand_distribution(distr_criteria):
                    found = True
                    self.index = index
                    break
            if found:
                self.solution_found = True
                self.deal = deal
                break
            i = i + 1
        self.count = i


selection_criteria='none', hcp_criteria=[13,15], ltc_criteria=[7,8], distr_criteria=[3,3,3,4]
    def __repr__(self):
        result.append('')
        result.append('HandSelection')
        result.append('selection_criteria: %s, hcp_criteria: %s, ltc_criteria: %s, distr_criteria: %s' (selection_criteria, hcp_criteria, ltc_criteria, distr_criteria))   
        result.append
        output = ''
        for each in result:
            output = '%s\n%s' % (output, str(each))
        return output


    def __get_teams(self, single_index):
        hand_indexes = [0,1,2,3]
        hand_indexes.remove(self.index)
        return [(selected_hand_index, hand_indexes[0]), (hand_indexes[1], hand_indexes[2])]




class PartnershipOnlySelection:
    """
        partnership_criteria: 'hcp' or 'distr' or 'hcp_distr' or 'none' 
    """

    def __init__(self, partnership_selection_criteria='none', partnership_hcp_criteria=[20,25], partnership_distr_criteria=[6,6,6,8]): 

        #partnership_hcp_criteria

        self.deal = ''
        self.teams = [('',''), ('','')]
        self.partnership_selection_criteria = partnership_selection_criteria
        self.partnership_hcp_criteria = partnership_hcp_criteria
        self.partnership_distr_criteria = partnership_distr_criteria
        self.index = -1     # not found
        self.count = 0      # number of itterations
        if self.partnership_selection_criteria=='none':
            self.none_selection()
        elif self.partnership_selection_criteria=='hcp':
            self.hcp_selection(partnership_hcp_criteria)


    def none_selection(self):
        deal = deal_cards()
        self.deal = deal
        self.index = 0
        self.teams = [(0,1),(2,3)]

    def hcp_selection(self, partnership_hcp_criteria):
        found = False
        i = 1
        while i <= MAX_ITERATIONS:
            deal = deal_cards()
            hand_0 = Hand(deal[0])
            hand_1 = Hand(deal[1])
            hand_2 = Hand(deal[2])
            hand_3 = Hand(deal[3])
            partnership_hcp = hand_0.hcp_total + hand_1.hcp_total
            if self.__select_partnership_hcp(partnership_hcp_criteria, partnership_hcp):
                found = True
                self.teams =  [(0,1),(2,3)]
                self.index = 0
                break
            partnership_hcp = hand_0.hcp_total + hand_2.hcp_total
            if self.__select_partnership_hcp(partnership_hcp_criteria, partnership_hcp):
                found = True
                self.teams = [(0,2),(1,3)]
                self.index = 0
                break
            partnership_hcp = hand_0.hcp_total + hand_3.hcp_total
            if self.__select_partnership_hcp(partnership_hcp_criteria, partnership_hcp):
                found = True
                self.index = index = [(0,3),(1,2)]
                self.index = 0
                break
            partnership_hcp = hand_1.hcp_total + hand_2.hcp_total
            if self.__select_partnership_hcp(partnership_hcp_criteria, partnership_hcp):
                found = True
                self.index = index = [(1,2),(0,3)]
                break
            partnership_hcp = hand_1.hcp_total + hand_3.hcp_total
            if self.__select_partnership_hcp(partnership_hcp_criteria, partnership_hcp):
                found = True
                self.index = index = [(1,3),(0,2)]
                break
            partnership_hcp = hand_2.hcp_total + hand_3.hcp_total
            if self.__select_partnership_hcp(partnership_hcp_criteria, partnership_hcp):
                found = True
                self.index = index = [(2,3),(0,1)]
                break

        self.count = i      # number of itterations
        if found:
            self.deal = deal
        else:
            self.index = -1

    def __select_partnership_hcp(self, bounds, partnership_hcp):
        """
            pass bounds [lb(lower bound), ub (upper bound)]
            returns true if band met
        """
        lb = bounds[0]
        ub = bounds[1]
        if partnership_hcp >= lb and partnership_hcp <= ub:
            return True
        return False

class HandAndPartnershipSelection:

    def __init__(self, hand_selection_criteria='hcp', hand_hcp=[13,15], hand_distr=[3,3,3,4],
                 partnership_selection_criteria='hcp', partnership_hcp=[20,25], partnership_distr=[6,6,6,8]): 
        """
            hand_selection_criteria: 'hcp', 'distr', 'hcp_distr', 'none'
            partnership_selection_criteria: 'hcp', 'distr', 'none'
        """
        self.deal = ''
        # teams = [ (selected partnership indexes), (other partnership index) }
        self.teams = [('',''), ('','')]
        self.partnership_found = False
        # hand description
        self.hand_selection_criteria = hand_selection_criteria
        self.hand_hcp = hand_hcp
        self.hand_distr = hand_distr
        # partnership description
        self.partnership_selection_criteria=partnership_selection_criteria
        self.partnership_hcp=partnership_hcp
        self.partnership_distr=partnership_distr
        if hand_selection_criteria <> 'none':
            i = 1
            while i <= 1000:
                # first select the hand
                hs = HandSelection(hand_selection_criteria, hand_hcp, hand_distr)
                if hs.index == -1:
                    # no hand can be found and selected
                    pass
                else:
                    # found a hand, now find a suitable partnership
                    self.check_partnership(hs.deal, hs.index, partnership_selection_criteria, partnership_hcp, partnership_distr)
                    if self.partnership_found:
                        break
                i = i + 1    
        elif hand_selection_criteria == 'none':
            pass


    def check_partnership(self, deal, selected_hand_index, partnership_selection_criteria, partnership_hcp, partnership_distr):
        """
            selected hand in deal[index]
            test parnership between selected hand and other hands

            updates
                self.parnership_found = True if partnership found
                self.teams = [(selected_hand_index, index), tuple(hand_indexes)]
                self.deal if partnership found else ''

            returns True (if partnership found) or False
        """
        found = False
        hand_indexes = [0,1,2,3]
        hand_indexes.remove(selected_hand_index)
        for index, item in enumerate(deal):
            # check partnerships
            # selected_hand_index with [hand_indexes]
            partnership = Partnership(hand=Hand(deal[selected_hand_index]), partner_hand=Hand(deal[index]))              
            if partnership.select_partnership_hcp(partnership_hcp) and partnership_selection_criteria=='hcp':
                # hcp partnership match
                found = True
                break
            elif partnership.select_partnership_distribution(partnership_distr) and partnership_selection_criteria=='distr':
                # partnership distriution match
                found = True
                break
            elif partnership_selection_criteria=='hcp_distr':
                if partnership.select_partnership_hcp(partnership_hcp) and partnership.select_partnership_distribution(partnership_distr):
                    # hcp and distribution partnership match
                    found = True
                    break
            elif partnership_selection_criteria=='none':
                # partnership match is not required
                hand_indexes.remove(index)
                self.teams = [(selected_hand_index, index), tuple(hand_indexes)]
                return True
        if found:
            self.parnership_found = True
            hand_indexes.remove(index)
            self.teams = [(selected_hand_index, index), tuple(hand_indexes)]
            self.deal = deal
            return True
        else:
            return False


def make_hands(deal, teams):
    """
        deal: original deal of all 4 hands
        teams: [ (team1), (team2) ]
    """
    h1 = Hand(deal[teams[0][0]])
    h2 = Hand(deal[teams[0][1]])
    h3 = Hand(deal[teams[1][0]])
    h4 = Hand(deal[teams[1][1]])
    return h1,h2,h3,h4

    


"""
    Test all scenarios
"""

selection_type = 'hand_only'
if selection_type == 'hand_only':
    print 'test1 - none'
    hs = HandSelection(selection_criteria='none')
    if hs.solution_found:
        h1,h2,h3,h4 = make_hands(hs.teams)






#selection_type = 'partnership_only'
#selection_type = 'hand_and_partnership'
if selection_type == 'partnership_only':
    # combined hcp or distr
    ps = PartnershipOnlySelection(partnership_selection_criteria='hcp')
    print ps.count
    print ps.index


if selection_type == 'hand_and_partnership':
    hp = HandAndPartnershipSelection()
    hp = HandAndPartnershipSelection(partnership_selection_criteria='hcp_distr')
    h1 = Hand(hp.deal[hp.teams[0][0]])
    h2 = Hand(hp.deal[hp.teams[0][1]])
    h3 = Hand(hp.deal[hp.teams[1][0]])
    h4 = Hand(hp.deal[hp.teams[1][1]])
    p = Partnership(h1,h2)
    




