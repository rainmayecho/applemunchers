def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def rcheck(n,primes):
    if n == 0:
        return True
    if n not in primes:
            return False
    else:
        return rcheck(n/10,refined)

def lcheck(n,refined):
    if n == 0:
        return True
    if n not in primes:
            return False
    else:
        i = int(str(n)[0])
        p = len(str(n))-1
        n -= i*10**p
        return lcheck(n,refined)

primes = get_primes(800000)
refined = []
for x in primes:
    y = [int(z) for z in str(x)]
    a = set([2,4,6,8,0,5])
    b = [c in y for c in a]
    if not any(b):
        refined.append(x)

final = [23,53]
for i in refined:
    if rcheck(i,refined) and lcheck(i,refined):
        final.append(i)

final.remove(3)
final.remove(7)
final.sort()

print sum(list(set(final)))
print final


