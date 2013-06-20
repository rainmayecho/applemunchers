import time, math
from Useful import get_primes, digit_sum, is_prime
from itertools import izip, count

def is_niven(n):
    d = digit_sum(n)
    if not n % d:
        return True
    return False
def is_strong(n):
    d = digit_sum(n)
    if is_prime(n/d):
        return True
    return False
def is_rt(n):
    while n > 10:
        if is_niven(n):
            n /= 10
        else:
            return False
    return True

primes = get_primes(10000)
cand = [n/10 for n in primes]

s = 0
for n, p in izip(cand[4:],primes[4:]):
    if is_rt(n) and is_strong(n):
        s += p
print s
