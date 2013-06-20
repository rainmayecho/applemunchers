import itertools

def is_prime(a):
    for x in range(2,int(a**.5)+1):
        if a%x==0:
            return False
    else:
        return True
    
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def is_circular(n, primes):
     i = 1
     also_prime = []
     if len(str(n)) == 1:
         return [n]
     if any(['2','4','5','6','8','0']) in list(str(n)):
         return also_prime
     while i < len(str(n)):
        n = int(str(n%10)+str(n/10))
        if is_prime(n):
            also_prime.append(n)
        else:
            return []
        i+=1
     return also_prime


primes = get_primes(1000000)
circular = [2,3,5,7]
for n in primes:
    if n in circular:
        continue
    c = is_circular(n,primes)
    if len(c)+1 == len(str(n)):
        c.append(n)
        circular.extend(list(set(c)))

print len(circular)
