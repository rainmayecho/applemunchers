def create_primes():
    primes = []
    for x in range(2,20):
        if is_prime(x):
            primes.append(x)
    return primes

        
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

def inverse_list():
    listA = []
    for x in range(1,21):
        if x not in create_primes():
            listA.append(x)
    pmsum = 1
    for x in create_primes():
        pmsum *= x
    print listA
    print pmsum
