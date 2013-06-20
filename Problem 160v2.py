import math
f = 1
n = 100
zeros = 0
p = 1
while True:
    val =  n/(5**p)
    if val:
        zeros += val
        p += 1
    else:
        break

m = int(math.log(n,10))

for z in xrange(2,11):
    f *= pow(z,2,10**5)
    print f

print f/10**zeros

