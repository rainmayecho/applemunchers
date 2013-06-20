k = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
     'T':10,'J':11,'Q':12,'K':13,'A':14}
f = open('poker.txt','r')
poker = [line.strip() for line in f]
p1 = [e[:15].replace(' ','') for e in poker]
p2 = [e[15:].replace(' ','') for e in poker]
for x in p1:
    x.replace('0','')
for x in p2:
    x.replace('0','')

def rf(hand,k):
    rank = []
    for i in range(0,len(hand)-1,2):
        rank.append((k[hand[i]],hand[i+1]))
    rank.sort()
    suit = rank[0][1]
    if rank[0][0]==10:
        prev = rank[0][0]
    else:
        return 0
    for x in rank:
        if x[1]==suit:
            continue
        else:
            return 0
        if x[0]-1 == prev:
            prev = x[0]
            continue
        else:
            return 0
    return 114

def sf(hand,k):
    if straight(hand,k) and flush(hand,k):
        return 113
    else:
        return 0

def four(hand,k):
    rank = []
    for i in range(0,len(hand)-1,2):
        rank.append((hand[i],0))
    rank.sort()
    poss1 = list(set(rank[1:]))
    poss2 = list(set(rank[0:-1]))
    if len(poss1)==1 or len(poss2)==1:
        return 112
    else:
        return 0

def fh(hand,k):
    rank = []
    for i in range(0,len(hand)-1,2):
        rank.append(hand[i])
    rank.sort()
    if rank[0]==rank[1] and rank[0]==rank[2]:
        val = k[rank[0]]
        if rank[3]==rank[4]:
            return 97+val
    if rank[2]==rank[3] and rank[2]==rank[4]:
        val = k[rank[2]]
        if rank[0]==rank[1]:
            return 97+val
    return 0

def flush(hand,k):
    rank = []
    for i in range(0,len(hand)-1,2):
        rank.append(hand[i+1])
    rank = list(set(rank))
    if len(rank)==1:
        return 96
    return 0
    
def straight(hand,k):
    rank = []
    for i in range(0,len(hand)-1,2):
        rank.append(k[hand[i]])
    rank.sort()
    prev = rank[0]
    for x in rank[1:]:
        if x-1==prev:
            prev = x
            continue
        else:
            return 0
    return 95


def three(hand,k):
    rank = []
    for i in range(0,len(hand)-1,2):
        rank.append(hand[i])
    rank.sort()
    if rank[0]==rank[1] and rank[0]==rank[2]:
        return 80
    if rank[2]==rank[3] and rank[2]==rank[4]:
        return 80
    if rank[1]==rank[2] and rank[1]==rank[3]:
        return 80
    return 0

def tp(hand,k):
    rank = []
    for i in range(0,len(hand)-1,2):
        rank.append(hand[i])
    seen = set()
    for n in rank:
        if n in seen:
            val = k[n]
        else:
            seen.add(n)
    rank = list(set(rank))
    if len(rank)==3:
        return 65
    return 0

def op(hand,k):
    rank = []
    for i in range(0,len(hand)-1,2):
        rank.append(hand[i])
    seen = set()
    for n in rank:
        if n in seen:
            val = k[n]
            break
        else:
            seen.add(n)
    rank = list(set(rank))
    if len(rank)==4:
        return 50+val
    return 0

def hc(hand,k,exc = None):
    m = 0
    rank = []
    for i in range(0,len(hand)-1,2):
        rank.append(hand[i])
    for x in rank:
        if k[x[0]] > m and not k[x[0]]==exc :
            m = k[x[0]]
    return m

def check(hand,k):
    s = rf(hand,k)
    if s:
        return s
    s = sf(hand,k)
    if s:
        return s
    s = four(hand,k)
    if s:
        return s
    s = fh(hand,k)
    if s:
        return s
    s = flush(hand,k)
    if s:
        return s
    s = straight(hand,k)
    if s:
        return s
    s = three(hand,k)
    if s:
        return s
    s = tp(hand,k)
    if s:
        return s
    s = op(hand,k)
    if s:
        return s
    return hc(hand,k)

def contest(hand,k,exc):
    return hc(hand,k,exc)

p1wc = 0
for x in range(len(p1)):
    rp1 = check(p1[x],k)
    rp2 = check(p2[x],k)
    if rp1>rp2:
        p1wc+=1
    while rp1==rp2:
        rp1 = contest(p1[x],k,rp1)
        rp2 = contest(p2[x],k,rp2)
        if rp1>rp2:
            p1wc+=1

print p1wc
