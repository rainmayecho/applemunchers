from Useful import*
import itertools

primes = sieve(int((10**3)))
poss = [x[0]*x[1] for x in list(itertools.product(primes,primes))]
print poss

least = [100.0,0]
for x in poss:
    a = phi(x)
    r = float(x/a)
    if r >= least[0]:
        continue
    b = [int(e) for e in str(a)]
    b.sort()
    c = [int(e) for e in str(x)]
    c.sort()
    if b == c:
        print x,a
        least[0] = r
        least[1]=x

print least[1]
