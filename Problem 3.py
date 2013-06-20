import time

def create_primes():
    primes = []
    for x in range(2,12375):
        if is_prime(x):
            primes.append(x)
    return primes

def is_prime(a):
    if a==2:
        return True
    if a==3:
        return True
    if a<2:
        return False
    if a==5:
        return True
    if a==7:
        return True
    for x in range(2,int(a**.5+1)):
        if a%x==0:
            return False
    else:
        return True

time.clock()

plist = create_primes()
pfact = []
num = 600851475143
for x in plist:
    if num%x==0:
        pfact.append(x)
print max(pfact)
print str(time.clock()*1000)+"ms"
          
            
        
