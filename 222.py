##Problem 222

import math

sv = 0
for r in range(30,51):
    sv += 4/3*r**3*math.pi

minlen = sv/(50**2*math.pi)
print minlen*1000

radii = range(30,51)
radii1 = range(30,51)
length = 0
for r in radii:
    r1 = radii1.pop()
    length += ((r+r1)**2-(r1-r)**2)**.5

print length*1000
    
