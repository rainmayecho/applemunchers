from itertools import *

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def check(a):
    ans = []
    for i in a:
        b = list(str(i))
        b.sort()
        ans.append(b)
    if ans[0] == ans[1] and ans[0]==ans[2]:
        return True
    return False
        

primes = get_primes(9999)
k = 3330
ans = []

for x in range(1000,3333):
    if x in primes:
        if x+k in primes:
            if x+2*k in primes:
                a = [x,x+k,x+2*k]
                if check(a):
                    ans.append(a)
print ans

