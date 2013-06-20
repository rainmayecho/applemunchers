import itertools

def manhattan(r):
    total = 0
    smr = [pow(n,2) for n in range(0,r+1)]
    c = list(itertools.combinations_with_replacement(smr,3))
    for e in c:
        if sum(e) == r**2:
            print e
            total += e[0]**.5 + e[1]**.5 + e[2]**.5
    return total*8

print manhattan(45)
    
