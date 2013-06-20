import time

time.clock()
t = 1
hypx = 1855
base = 1777
while hypx:
    t = pow(base,t,10**8)
    hypx -= 1

print t
print str(time.clock()*1000)+'ms'
