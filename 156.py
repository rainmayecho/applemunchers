import math
def f(n,d):
    if n:     
        e = int(math.log(n,10))
    else:
        e = 1
    count = 0
    i = 1
    while i <= e:
        count += (n/10**(i))*10**(i-1)
        i += 1
    return count


for n in xrange(12):
    print f(n,1)
