from Useful import get_primes
import math, time



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

time.clock()
lim = int(math.floor(math.log(2*10**6,3)))
primes = get_primes(50)
p1 = 1
p2 = 1
for e in primes[:lim-1]:
    p1 *= e
    p2 *= e
p2 *= primes[lim-1]*primes[lim]

n = p1
while n < p2:
    a = analyze(factorize(n**2,primes)[1])
    if a > 8*10**6:
        print n, a
        break
    n += p1

print str(time.clock()*1000)+'ms'
