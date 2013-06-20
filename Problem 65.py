import time
from Useful import*

time.clock()
seclist = [2]
t = 1
for n in range(1,100):
    sec = 1
    if (n+1)%3==0:
        sec = 2*t
        t+=1
    seclist.append(sec)

d = addfrac((seclist[-1],1),(0,1))
flag = True
for x in seclist[::-1]:
    if flag:
        flag = False
        continue
    d = addfrac((x,1),inv(d))

print sum([int(x) for x in str(d[0])])
print str(time.clock()*1000)+"ms"
