import math
from Useful import get_primes
def factorize(n, primes):
    temp = n
    t = [0 for x in range(len(primes))]
    for i in xrange(len(t)):
        while temp > 1 and temp % primes[i] == 0:
            t[i] += 1
            temp /= primes[i]
        if temp == 1:
            return True, t, temp
    return False, t, temp

def analyze(fcount):
    use = [n for n in fcount if n]
    p = 1
    for e in use:
        p *= (e + 1)
    return p
    
primes = get_primes(100000)
n = 30030
while n < 510510:
    a = analyze(factorize(n**2,primes)[1])
    if a > 2000:
        print n
        break
    n += 30030

