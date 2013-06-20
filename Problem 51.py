import string
from string import whitespace, digits

def sieve(n):
    sieve = range(n+1)
    sieve[1] = 0
    for i in range(2, int(n**.5)+1):
        if sieve[i]:
           m = n/i - i
           sieve[i*i: n+1:i] = [0] * (m+1)
    return [x for x in sieve if x]

def f(n):
    if len(list(set(str(n)))) < len((str(n))):
        return n
    else:
        return 0
def remove_dup(n):
    return ''.join([c for i, c in enumerate(n) if c in whitespace \
             or not c in n[:i]])
    
def r(n):
    a = str(n)
    b = remove_dup(a)
    for x in b:
        a = a.replace(x,"",1)
    return int(a)


def allindices(string, sub, listindex=[], offset=0):
    i = string.find(sub, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(sub, i + 1)
    return listindex


primes = sieve(1000000)
cand = filter(f,primes)
seen = []
for x in cand:
    d = 0
    if x < 100000:
        continue
    for i in list(set(str(x))):
        c = 0
        for y in range(0,10):
            if int(i)==y:
                continue
            a = str(x)
            a = a.replace(i,str(y))
            if a == '':
                continue
            if a[0]=='0':
                continue
            if int(a) in primes:
                c+=1
        if c+(10-y) < 7:
            break
        if c == 7:
            d = c
            break
        
    if d == 7:
        print x
        break
