def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def pfactorize(a,primes,b,pfactors = []):
    if a==1:
        return pfactors
    if a==2:
        pfactors.append(2)
        return pfactors
    if a==3:
        pfactors.append(3)
        return pfactors
    for x in primes:
        if a%x==0:
            pfactors.append(x)
    prod = 1
    for y in pfactors:
        prod *= y
    if not prod == b:
        pfactorize(b/prod,primes,b,pfactors)
    return pfactors

primes = get_primes(1000000)
count = 0
fourfact = []
for x in range(133000,1000000):
    numfactors = len(list(set(pfactorize(x,primes,x,[]))))
    if x in primes:
        continue
    if numfactors == 4:
        count += 1
    else:
        count = 0
    if count == 4:
        print x-3
        break




