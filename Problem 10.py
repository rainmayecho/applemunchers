import math

def is_prime(a):
    if a==2:
        return True
    for x in range(2,a**.5+1):
        if a%x==0:
            return False
    else:
        return True

def sum_prime():
    sumPrime = 0
    for x in range(2,2000):
        if is_prime(x):
            sumPrime += x
    print sumPrime
            
    


