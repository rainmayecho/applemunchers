from Useful import phi, get_primes ,gcd


count = 0
for n in xrange(1, 1000001/2):
    if gcd(1000001-n,n) == 1:
        count += 1
print count/2
