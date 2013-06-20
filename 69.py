import time

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

time.clock()
primes = get_primes(20)
n = 1
i = 0
while n < 1000000:
    temp = n
    n*=primes[i]
    if n > 1000000:
        n = temp
        break
    i+=1
print n
print str(time.clock()*1000)+"ms"
    

    
            
            
