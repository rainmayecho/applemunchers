def create_primes():
    primes = []
    for x in range(2,1000000):
        if is_prime(x):
            primes.append(x)
    print primes[10000]
        
def is_prime(a):
    if a==2:
        return True
    if a<2:
        return False
    for x in range(2,a**.5+1):
        if a%x==0:
            return False
    else:
        return True
