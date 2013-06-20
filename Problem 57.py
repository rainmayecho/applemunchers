import time

time.clock()
fract = (1,1)
count = 0
for i in range(1,1000):
    fract = (2*fract[1]+fract[0],fract[0]+fract[1])
    if len(str(fract[0])) > len(str(fract[1])):
        count += 1
print count
print str(time.clock()*1000)+"ms"

## Brute-Force, Best runtime ~19.7 ms , compared to alternate best ~8.28 ms
