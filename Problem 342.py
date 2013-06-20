import itertools,operator

def sieve(n):
    sieve = range(n+1)
    sieve[1] = 0
    for i in xrange(2, int(n**.5)+1):
        if sieve[i]:
           m = n/i - i
           sieve[i*i: n+1:i] = [0] * (m+1)
    return [x for x in sieve if x]

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

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def phi(n):
    c = 1
    if n%2==0:
        for x in range(3,n,2):
            if gcd(x,n)==1:
                c+=1
    else:
        for x in range(2,n):
            if gcd(x,n)==1:
                c+=1
    return c

primes = sieve(100000)
pfactors = pfactorize(2500,primes,2500,[])
npfactors = [reduce(operator.mul,j)
                     for i in range(2,len(pfactors)+1)
                     for j in itertools.combinations(pfactors,i)]
print list(set(npfactors))


sqr = []
cube = []
for x in range(1,1000):
    sqr.append(x**2)
    cube.append(x**3)
s = 0
for x in sqr:
    n = int(x**.5)
    if n*phi(n) in cube:
        s+= n
print s
    
