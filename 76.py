import itertools, math, time

time.clock()
arg = 100
z = range(1,100)
ways = [1]+[0]*arg

for i in z:
    for j in range(i,arg+1):
        ways[j]+= ways[j-i]

print max(ways)
print str(time.clock()*1000)+"ms"
