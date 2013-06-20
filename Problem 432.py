import math, time
from Useful import is_prime, gcd

def phi(n):
    p = 0
    for i in xrange(n):
        if gcd(n,i) == 1:
            p += 1
    return p

def ec_phi(n, d):
    if is_prime(n):
        return n-1

    if not n % d:
        if is_prime(d):
            q = n / d
            return (d-1)*ec_phi(q, int(q**.5) + 1)

    return ec_phi(n, d-1)
        
def s(n, m):
    r = 0
    for i in xrange(1, m):
        r += phi((n*i)% 10**6)
        print i
    return r

print ec_phi(100,11)
print phi(100)
    

