import time

time.clock()

n = 2
t = 1
count = 3
while n <= 10**999:
    t1 = n
    n+=t
    t = t1
    count+= 1
print count
print str(time.clock()%1000)+"ms"
