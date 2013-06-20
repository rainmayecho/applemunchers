from Useful import sieve, ext_gcd
import math

primes = sieve(1000005)

summation = 0
for i in xrange(2, len(primes)-1):
    p1 = primes[i]
    p2 = primes[i+1]
    n = p2
    nd = len(str(p1))
    a = 10**nd
    b = p2 - p1
    r, s, d = ext_gcd(a,n)
    x = r*b
    x = (x % n)*a + p1
    summation += x
    
print summation
