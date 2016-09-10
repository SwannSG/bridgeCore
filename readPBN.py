# read and write Portable Bridge Notation

# deal
#   n e s w
#   s h d c

import re
import hashlib

p1 = re.compile(r'^\[([a-zA-z]*)[ ]+"([a-zA-Z0-9\' .:]+)"')

srcFolder = '/home/swannsg/development/bridge/pbn'
fname = 'Aulpll23.pbn'
fp = open(srcFolder + '/' + fname, 'r')

collection = []
start = True
i = 0
for l in fp:        # l = line

    if l.strip()=='*' or start:
        # start of new hand
        if not start:
            doc['hash'] = hashlib.sha1(bytes(strToHash, 'utf-8')).hexdigest()
            collection.append(doc)
            i = i + 1
        doc = {}
        auction = []
        play = []
        key = ''
        strToHash = ''
        start = False


    r = re.search(p1, l)
    if r is not None:
        key = r.groups()[0]
        value = r.groups()[1]
        doc[key] = value
        strToHash = strToHash + key + value
    else:
        if key=='Auction':
            auction.append(l.strip().split(' '))
            doc['AuctionSeq'] = auction
            strToHash = strToHash + l.strip()
        elif key=='Play':
            play.append(l.strip().split(' '))
            doc['PlaySeq'] = play
            strToHash = strToHash + l.strip()
fp.close()
print (collection[0])
