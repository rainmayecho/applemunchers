import itertools

def is_pent(x):
    n = ((24*x+1)**.5+1)/6.0
    if n == int(n):
        return True
    return False

def pent(n):
    return n*(3*n-1)/2

penta = [pent(n) for n in range(1,4000)]
combs = list(itertools.permutations(penta,2))
sumcomb = [sum(x) for x in combs]
diffcomb = [(x[1]-x[0]) for x in combs]

for i in range(0,len(combs)):
    if is_pent(sumcomb[i]) and is_pent(abs(diffcomb[i])):
        print abs(diffcomb[i])
        break


