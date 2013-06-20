import itertools, time

def create_primes():
    primes = []
    for x in range(2,999):
        if is_prime(x):
            primes.append(x)
    return primes

def is_prime(a):
    if a<2:
        return False
    if a==2:
        return True
    if a==3:
        return True
    if a%2==0:
        return False
    if a==5:
        return True
    if a==7:
        return True
    for x in range(3,int(a**.5+1)):
        if a%x==0:
            return False
    else:
        return True

def quadratic(pair):
    a = pair[0]
    b = pair[1]
    for n in range(0,80):
        if is_prime(n*n+(a*n)+ b):
            continue
        else:
            return n

time.clock()

coeff = [1]
primes = create_primes()

for x in primes:
    coeff.append(x)
    coeff.append(-x)
coeff.sort()
permutations = list(itertools.permutations(coeff,2))
counts = []

for pair in permutations:
    c = quadratic(pair)
    counts.append(c)

m = max(counts)
i = counts.index(m)
print permutations[i]
print m
print str(time.clock()*1000)+"ms"
    
    
    
    
