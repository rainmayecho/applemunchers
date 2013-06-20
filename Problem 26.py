import time

def denom(d):
    numerators = []
    incomplete = True
    n = 1
    while incomplete:
        while n < d:
            n *= 10
        numerators.append(n%d)
        e = n/d
        n = n%(d*e)
        flag = numerators[-1] in numerators[0:-1]
        if flag:
            incomplete = False
            return len(numerators[0:-1])
        elif n == 0:
            incomplete = False
            return 0
t1 = time.time()
r = []
for d in range(1,1000):
    r.append(denom(d))
print r.index(max(r))+1
print str((time.time()-t1)*1000)+"ms"
            
        
        
