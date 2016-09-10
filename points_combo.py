import itertools as t


def score(l):
    d = {'A':4, 'K':3, 'Q':2, 'J':1}
    hcp = 0
    if not l:
        return 0
    for each in l:
        hcp = hcp + d[each]
    return hcp

s = set(['A', 'K', 'Q', 'J'])
r = list()

i_1 = t.combinations(s,1)
i_2 = t.combinations(s,2)
i_3 = t.combinations(s,3)
i_4 = t.combinations(s,4)

each = []
diff = s.difference(set(each))
i = 0
while i <= len(diff): 
    comb = t.combinations(diff,i)
    for item in comb:
        r.append((tuple(each), tuple(item)))
    i = i + 1

for each in i_1:
    diff = s.difference(set(each))
    i = 0
    while i <= len(diff): 
        comb = t.combinations(diff,i)
        for item in comb:
            r.append((tuple(each), tuple(item)))
        i = i + 1

for each in i_2:
    diff = s.difference(set(each))
    i = 0
    while i <= len(diff): 
        comb = t.combinations(diff,i)
        for item in comb:
            r.append((tuple(each), tuple(item)))
        i = i + 1

for each in i_3:
    diff = s.difference(set(each))
    i = 0
    while i <= len(diff): 
        comb = t.combinations(diff,i)
        for item in comb:
            r.append((tuple(each), tuple(item)))
        i = i + 1

for each in i_4:
    diff = s.difference(set(each))
    i = 0
    while i <= len(diff): 
        comb = t.combinations(diff,i)
        for item in comb:
            r.append((tuple(each), tuple(item)))
        i = i + 1

for each in r:
    print each
    

        
c = list()
i = 0
while i < len(r):
    c.append((score(r[i][0]), score(r[i][1]))) 
    i = i + 1

c.sort()
d = dict()
n = ''
for each in c:
    if each[0] <> n:
        print ''
        print 'key: %s' % each[0]
        d[each[0]] = list()
        print 'value: %s' % each[1]
        d[each[0]].append(each[1])
        n = each[0]
    else:
        print 'value: %s' % each[1]
        d[each[0]].append(each[1])

print c
for each in d:
    d[each] = list(set(d[each]))
    
