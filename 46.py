import itertools

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

primes = get_primes(10000)
twicesq = [2*x**2 for x in range(1,1000)]
oddcomp = [2*n-1 for n in range(2,1000000) if 2*n-1 not in primes]
poss = []
for x in primes:
    for y in twicesq:
        poss.append(x+y)

poss = list(set(poss))
poss.sort()
for x in oddcomp:
    if x not in poss:
        print x
        break
