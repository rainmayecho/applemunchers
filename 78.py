from Useful import pent
import time

def gen_pent(n):
    if n < 0 :
        return 0
    if n % 2 == 0:
        return pent(n/2+1)
    else:
        return pent(-(n/2+1))
    
time.clock()
partitions = [1]
for n in range(1,100000):
    r = 0
    f = -1
    i = 0
    while True:
        k = gen_pent(i)
        if k > n:
            break
        if i % 2==0:
            f = -f
        r += f*partitions[n-k]
        i += 1
    partitions.append(r)
    if r % 10**6 == 0:
        print n
        break
print str(time.clock())+'s'

