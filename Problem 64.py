##Problem 64
import time

time.clock()
sqrs = [n**2 for n in range(1,101)]
nlist = [n for n in range(1,10001) if n not in sqrs]
count = 0

for n in nlist:
    a =int(n**.5)
    ao=int(n**.5)
    d = 1
    m = 0
    triplet = []
    while True:
        m = d*a-m
        d = (n-m**2)/d
        a = int((ao+m)/d)
        triplet.append((m,d,a))
        triplet.sort()
        repeatcheck = list(set(triplet))
        repeatcheck.sort()
        if not repeatcheck == triplet:
            if not len(repeatcheck) % 2 == 0:
                count += 1
            break
print count
print str(time.clock())+'s'

