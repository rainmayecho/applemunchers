import Useful
def has_mult(ps):
    for i,e in enumerate(ps):
        if e in ps[0:i]:
            return False
    return True
primes = Useful.sieve(10**7)

check = range(1,10)
remain = list(check)
count = 0
setsize = 2
while setsize < 10:
    for p in primes:
        ps = [int(n) for n in str(p)]
        ps.sort()
