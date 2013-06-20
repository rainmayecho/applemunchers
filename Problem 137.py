import time

def fib(tup):
    return (tup[1],sum(tup))

time.clock()
t = (1,1)
n = 15

for i in xrange(1, 2*n):
    t = fib(t)

print t[0]*t[1]
print str(time.clock()*1000)+'ms'
