import random
from bridge_utils import *

class pattern:
    """
        '*' is an "any wildcard"
        own: your hand that will match reqested pattern

        own_distr = (nC, nD, nH, nS)
        own_points = (hcpC, hcpD, hcpH, hcpS)
            or
        own_HCP = HCP for the hand

        team_distr  = (nC, nD, nH, nS) for the partnership (team)
        team_points = (hcpC, hcpD, hcpH, hcpS) for the partnership
            or
        team_HCP = HCP for the partnership  

        b_own_distr=True: own distribution is a selection criteria
        b_own_points=True: own points is a selection criteria (includes own_HCP)
        b_team_distr=True: team distribution is a selection criteria
        b_team_points=True: team points is a selection criteria (includes team_HCP)
        
    """
    def __init__(self, own_distr='*', own_points='*',
                 own_HCP='*', team_distr='*',
                 team_points='*', team_HCP='*'):
        self.own_distr = own_distr
        self.own_points = self.adj_tuple_points(own_points, own_HCP)
        self.own_HCP = own_HCP
        self.team_distr = team_distr
        self.team_points = self.adj_tuple_points(team_points, team_HCP)
        self.team_HCP = team_HCP
        # selection criteria
        self.b_own_distr = False
        self.b_own_points = False
        self.b_team_distr = False
        self.b_team_points = False
        self.make_selection_criteria()

    def make_selection_criteria(self):
        self.b_own_distr = True if self.own_distr <> '*' else False
        if self.own_distr <> '*':
            if self.own_distr == ('*','*','*','*'):
                self.b_own_distr = False
            else:
                self.b_own_distr = True
        else:
            self.b_own_distr = False
        if self.own_points == '*' and self.own_HCP == '*':
            self.b_own_points = False
        else:
            self.b_own_points = True

        self.b_team_distr = True if self.team_distr <> '*' else False
        if self.team_points == '*' and self.team_HCP == '*':
            self.b_team_points = False
        else:
            self.b_team_points = True

    def adj_tuple_points(self, tuple_points, hcp):
        """
            if hcp = number
                tuple_points = '*' (overwrites existing tuple_points)
            else
                use user provided tuple points
        """
        if hcp <> '*':
            # total HCP overides own_points 
            return '*'
        else:
            return tuple_points
        





def deal():
    """
    randomly generate 4 hands
    """
    _range = range(1, 53)
    r = random.sample(_range, 52)
    return  (r[0:13], r[13:26], r[26:39], r[39:52])

def a_wildcard_b(numeric, pattern):
    """
        pass tuple a, b of same length = 4
        returns a tuple of same length = 4
            where '*' occurs
    """
    l = []
    for index, value in enumerate(pattern):
        if value == '*':
            l.append(value)
        else:
            l.append(numeric[index])
    return tuple(l)

def find_distribution_match(deal, pattern):
    """
        deal = tuple([hand_0], [hand_1], [hand_2], [hand_3])
        pattern = (nC, nD, nH, nS)

        if distribution(hand_x) == pattern
            return index to each deal i.e. 0,1,2,3
        else
            return False
    """
    for index, hand in enumerate(deal):
        distr = summary_of_distribution(hand)
        if a_wildcard_b(distr, pattern) == pattern: 
            return index
    return False

def find_points_match(deal, pattern, integer_HCP):
    """
        deal: tuple([hand_0], [hand_1], [hand_2], [hand_3])
        pattern: (hcp_C, hcp_D, hcp_H, hcp_S)
        integer_HCP: HCP for hand
    """
    if integer_HCP <> '*':
        # ignore tuple_points, just use HCP for hand
        for index, hand in enumerate(deal):
            if integer_HCP == hcp_for_cards(hand):
                return index
    else:
        # use tuple_points as pattern
        for index, hand in enumerate(deal):
            hcp_points_per_suit = hcp_distr(hand)
            if a_wildcard_b(hcp_points_per_suit, pattern) == pattern: 
                return index
    return False

def points_match(hand, pattern, integer_HCP):
    """
        hand: [hand]
    """
    if integer_HCP <> '*':
        # ignore tuple_points, just use HCP for hand
        if integer_HCP == hcp_for_cards(hand):
            return True
    else:
        # use tuple_points as pattern
        if a_wildcard_b(hcp_distr(hand), pattern) == pattern:
            return True
    return False

def NSWE(deal, index_to_exclude):
    """
        index_to_exlude: 0 <= integer <= 3
                            or
                         tuple(index_1, index_2)
        
    """
    if type(index_to_exclude) is int:
        N = index_to_exclude    
        S,W,E = [x for x in [0,1,2,3] if x not in [index_to_exclude]]
        return (deal[N],deal[S],deal[W],deal[E])
    if type(index_to_exclude) is tuple:
        N = index_to_exclude[0]
        S = index_to_exclude[1]
        W,E = [x for x in [0,1,2,3] if x not in list(index_to_exclude)]
        return (deal[N],deal[S],deal[W],deal[E])
        

def find_team_distribution_match(deal, pattern):
    """
        deal: tuple([hand_0], [hand_1], [hand_2], [hand_3])
        pattern: (nC, nD, nH, nS) for the team
    """
    a = {1:0, 2:0, 3:0, 4:1, 5:1, 6:2}
    b = {1:1, 2:2, 3:3, 4:2, 5:3, 6:3}
    deal_distr = deal_distribution(deal)
    i = 1
    while i <= 6:
        index_hand_1 = a[i]
        index_hand_2 = b[i]
        if a_wildcard_b(tuple([sum(x) for x in zip(deal_distr[0],deal_distr[1])]), pattern) == pattern:
            return (index_hand_1, index_hand_2)        
        i = i + 1
    return False






no_of_deals = 1000000
#p = pattern(own_points=(7, 3, 4, 6))
#p = pattern(own_distr=(3,3,3,4),own_points=(7,3,4,6))
#p = pattern(own_distr=(3,3,3,4),own_HCP=10)
p = pattern(team_distr=(6,6,6,8))

print 'b_own_distr: %s' % p.b_own_distr
print 'b_own_points: %s' % p.b_own_points
print 'b_team_distr: %s' % p.b_team_distr 
print 'b_team_points: %s' % p.b_team_points 

i = 1
while i <= no_of_deals:
    each_deal = deal()
    hand_match_index = -1

    if not (p.b_own_distr or p.b_own_points or p.b_team_distr or p.b_team_points):  
        # no selection criteria
        N,S,W,E = each_deal
        break

    if (p.b_own_distr and not p.b_own_points and not p.b_team_distr and not p.b_team_points):
        # own distribution
        hand_match_index = find_distribution_match(each_deal, p.own_distr)
        if hand_match_index:
            # distribution found
            N,S,W,E = NSWE(each_deal, hand_match_index) 
            break

    if not p.b_own_distr and p.b_own_points and not p.b_team_distr and not p.b_team_points:
        # own points
        hand_match_index = find_points_match(each_deal, p.own_points, p.own_HCP)
        if hand_match_index:
            # distribution found
            N,S,W,E = NSWE(each_deal, hand_match_index) 
            break

    if p.b_own_distr and p.b_own_points and not p.b_team_distr and not p.b_team_points:
        # own distribution and own points
        hand_match_index = find_distribution_match(each_deal, p.own_distr)
        if hand_match_index:
            # distribution found
            if points_match(each_deal[hand_match_index], p.own_points, p.own_HCP):
                # points_match
                # own_distr and own_points found
                N,S,W,E = NSWE(each_deal, hand_match_index) 
                break

    if not p.b_own_distr and not p.b_own_points and p.b_team_distr and not p.b_team_points:
        # team distribution
        hand_match_indexes = find_team_distribution_match(each_deal, p.team_distr)
        if hand_match_indexes:
            # team distribution found
            N,S,W,E = NSWE(each_deal, hand_match_indexes)
            break

    i = i + 1

if i > no_of_deals:
    print 'no hand found'
else:
    print 'i: %s' % i
    print 'hand integers: %s' % N
    print 'hand symbols: %s' % getSymbols(N)
    print 'summary_of_distribution N: %s' % str(summary_of_distribution(N))
    print 'hcp_distr: %s' % str(hcp_distr(N))
    print 'HCP: %s' % hcp_for_cards(N)

    print 'summary_of_distribution S: %s' % str(summary_of_distribution(S))
    


    
