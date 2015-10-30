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
        numeric: tuple(n1,n2,n3,n4)
        pattern: tuple(np1||'*',np2||'*',np3||'*',np4||'*')
        returns: (n1 or '*' if np1=='*', r2, r3, r4)

        ex1: a = (3,2,5,3), b = (4,4,*,*), r = (3,2,*,*) 

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

def find_points_match_in_one_hand(deal, indexes, pattern, integer_HCP):
    """
        deal = tuple([hand_0], [hand_1], [hand_2], [hand_3])
        pattern = (hcp_C, hcp_D, hcp_H, hcp_S)
                    or
        integer_HCP = '*' or integer
        indexes = (hand_index_1, hand_index_2)
        return = (north_hand_index, south_hand_index)
            where pattern match is for north hand
    """
    if integer_HCP <> '*':
        # ignore tuple_points, just use HCP for hand
        if hcp_for_cards(deal[indexes[0]]) == integer_HCP:
            return (indexes[0], indexes[1])
        if hcp_for_cards(deal[indexes[1]]) == integer_HCP:
            return (indexes[1], indexes[0])
    else:
        # use tuple_points as pattern
#        print pattern
#        print a_wildcard_b(hcp_distr(deal[indexes[0]]),pattern)
#        print a_wildcard_b(hcp_distr(deal[indexes[1]]),pattern)
#        print ''
        if a_wildcard_b(hcp_distr(deal[indexes[0]]),pattern) == pattern:
            return (indexes[0], indexes[1])
        if a_wildcard_b(hcp_distr(deal[indexes[1]]),pattern) == pattern:
            return (indexes[1], indexes[0])
    return False

def find_distribution_match_in_one_hand(deal, indexes, pattern):
    """
        deal = tuple([hand_0], [hand_1], [hand_2], [hand_3])
        pattern = (nC, nD, nH, nS)
        indexes = (hand_index_1, hand_index_2)
        return = (north_hand_index, south_hand_index)
            where pattern match is for north hand
    """
    if a_wildcard_b(summary_of_distribution(deal[indexes[0]]),pattern) == pattern:
        return (indexes[0], indexes[1])
    if a_wildcard_b(summary_of_distribution(deal[indexes[1]]),pattern) == pattern:
        return (indexes[1], indexes[0])
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
        return: matching indexes as tuple
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


def find_team_hcp_match(deal_hcp, integer_HCP):
    """
        deal_hcp: (HCP_hand_1, HCP_hand_2, HCP_hand_3, HCP_hand_4)
        integer_HCP: HCP for hand
        return: matching indexes as tuple
                or
                False
    """
    a = {1:0, 2:0, 3:0, 4:1, 5:1, 6:2}
    b = {1:1, 2:2, 3:3, 4:2, 5:3, 6:3}
    i = 1
    while i <= 6:
        index_hand_1 = a[i]
        index_hand_2 = b[i]
        if deal_hcp[index_hand_1] + deal_hcp[index_hand_2] == integer_HCP:
            return (index_hand_1, index_hand_2)
        i = i + 1
    return False

def find_team_hcp_tuple_match(dealHCPdistr, pattern):
    """
        dealHCPdistr: tuple((hcpC,D,H,S), (hcpC,D,H,S), (hcpC,D,H,S), (hcpC,D,H,S))
        pattern: (hcp_C, hcp_D, hcp_H, hcp_S) for team, both hands combined
        return: matching indexes as tuple
                or
                False
    """
    a = {1:0, 2:0, 3:0, 4:1, 5:1, 6:2}
    b = {1:1, 2:2, 3:3, 4:2, 5:3, 6:3}
    i = 1
    while i <= 6:
        index_hand_1 = a[i]
        index_hand_2 = b[i]
        sum_hand_1_2 = tuple([sum(x) for x in zip(dealHCPdistr[index_hand_1], dealHCPdistr[index_hand_2])])
        if a_wildcard_b(sum_hand_1_2, pattern) == pattern:
            return (index_hand_1, index_hand_2)        
        i = i + 1
    return False

def sum_tuple(tuple_1, tuple_2):
    """
        tuple_1 = (1,2,3,4)
        tuple_2 = (6,7,8,9)
        result = (7,9,11,13)
    """
    return tuple([sum(x) for x in zip(tuple_1, tuple_2)])


def find_team_points(deal, pattern, integer_HCP):
    """
        deal: tuple([hand_0], [hand_1], [hand_2], [hand_3])
        pattern: (hcp_C, hcp_D, hcp_H, hcp_S) for team, both hands combined
        integer_HCP: HCP for hand
    """
    if integer_HCP <> '*':
        # ignore tuple_points, just use HCP for both hands
        dealHCP = deal_hcp(deal)
        return find_team_hcp_match(dealHCP, integer_HCP)
    else:
        # use tuple_points as pattern
        dealHCPdistr = deal_hcp_distr(deal)
        return find_team_hcp_tuple_match(dealHCPdistr, pattern)

def team_points_match(deal, indexes, pattern, integer_HCP):
    """
        deal: tuple([hand_0], [hand_1], [hand_2], [hand_3])
        indexes: tuple(hand_x, hand_y)
        pattern: (hcp_C, hcp_D, hcp_H, hcp_S) for team, both hands combined
        integer_HCP: HCP for hand
    """
    if integer_HCP <> '*':
        # ignore tuple_points, just use HCP for both hands
        if hcp_for_cards(deal[indexes[0]]) + hcp_for_cards(deal[indexes[1]]) == teamHCP:
            return True
    else:
        # use tuple_points as pattern
        sum_hand_1_2 = sum_tuple(hcp_distr(deal[indexes[0]]), hcp_distr(deal[indexes[1]]))
        if a_wildcard_b(sum_hand_1_2, pattern) == pattern:
            return True
    return False


no_of_deals = 10000000
#p = pattern(own_points=(7, 3, 4, 6))
#p = pattern(own_distr=(3,3,3,4),own_points=(7,3,4,6))
#p = pattern(own_distr=(3,3,3,4),own_HCP=10)
#p = pattern(team_distr=(6,6,6,8))
#p = pattern(team_points=(5,5,5,5))
#p = pattern(team_distr=(6,6,6,8), team_points=(5,5,5,5))
#p = pattern(team_distr=(6,6,6,8), own_distr=(2,3,4,4))
p = pattern(own_HCP=5, team_HCP=15)

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
        # team distribution only
        hand_match_indexes = find_team_distribution_match(each_deal, p.team_distr)
        if hand_match_indexes:
            # team distribution found
            N,S,W,E = NSWE(each_deal, hand_match_indexes)
            break

    if not p.b_own_distr and not p.b_own_points and not p.b_team_distr and p.b_team_points:
        # team points only
        hand_match_indexes = find_team_points(each_deal, p.team_points, p.team_HCP)
        if hand_match_indexes:
            # team points found
            N,S,W,E = NSWE(each_deal, hand_match_indexes)
            break

    if not p.b_own_distr and not p.b_own_points and p.b_team_distr and p.b_team_points:
        # team distribution and team points
        hand_match_indexes = find_team_distribution_match(each_deal, p.team_distr)
        if hand_match_indexes:
            # team distribution match found
            if team_points_match(each_deal, hand_match_indexes, p.team_points, p.team_HCP):
            # team points match found
                N,S,W,E = NSWE(each_deal, hand_match_indexes)
                break
    if p.b_own_distr and not p.b_own_points and p.b_team_distr and not p.b_team_points:
        # own_distr and team_distr
        hand_match_indexes = find_team_distribution_match(each_deal, p.team_distr)
        if hand_match_indexes:
            # team distribution found
            north_south_indexes = find_distribution_match_in_one_hand(each_deal, hand_match_indexes, p.own_distr)
            if north_south_indexes:
                # own distribution found
                N,S,W,E = NSWE(each_deal, north_south_indexes)
                break

    if not p.b_own_distr and p.b_own_points and not p.b_team_distr and p.b_team_points:
        # own_points and team_points
        hand_match_indexes = find_team_points(each_deal, p.team_points, p.team_HCP)
        if hand_match_indexes:
            # team points found
            north_south_indexes = find_points_match_in_one_hand(each_deal, hand_match_indexes, p.own_points, p.own_HCP)
            if north_south_indexes:
                # own points found
                N,S,W,E = NSWE(each_deal, north_south_indexes)
                break

            
    i = i + 1

if i > no_of_deals:
    print 'no hand found'
else:
    print 'i: %s' % i
    print ''
    print 'North'
    print Hand(N)
    print 'South'
    print Hand(S)
    print 'Partnersip'
    print Partnership(N,S)
    
