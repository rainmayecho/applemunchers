import math
import time

time.clock()

f = open('base_exp.txt','r')
pairs = [[int(n) for n in s.split(',')] for s in f.readlines()]

maxpair = [1,1]
for e in pairs:
    x = math.log10(e[0])*e[1]
    if x > (math.log10(maxpair[0])*maxpair[1]):
        maxpair = e
print pairs.index(maxpair)+1
print str(time.clock()*1000)+"ms"
