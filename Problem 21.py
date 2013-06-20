import time

def div(n):
    divisors = []
    for i in range(1,n/2+1):
        if n%i==0:
            divisors.append(i)
    sumdiv = sum(divisors)
    return sumdiv

t1=time.time()
amicable = []
for n in range(1,10000):
    if div(div(n)) == n:
        if not div(n) == n:
            amicable.append(n+div(n))
print sum(set(amicable))
print str(time.time()-t1)+"s"
        
    
    
            
