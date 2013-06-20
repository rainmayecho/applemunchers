import time
time.clock()
a = []
for n in range(1,1000000):
    i=0
    while n>1:
        if n%2==0:
            n/=2
        else:
            n = 3*n+1
        i+=1
    a.append(i)
print a.index(max(a))+1
print str(time.clock()*1000)+" ms"

## Runtime-- 37.743 s
