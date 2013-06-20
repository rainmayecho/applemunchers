import time


def is_prime(n):
    if not n % 2:
        return False
    if not n % 3:
        return False
    for m in xrange(6,int(n**.5)+1, 6):
        if not n % (m+1):
            return False
        if not n % (m-1):
            return False
    return True

time.clock()
cubes = [n**3 for n in xrange(1,600)]
count = 0
for i in range(len(cubes)-1):
    n = cubes[i+1]-cubes[i]
    if is_prime(n):
        count += 1
    if n > 10**6:
        break
print count
print str(time.clock()*1000)+'ms'
        
        


    

