import time

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

time.clock()
ans = 0
for d in range(4,12001):
    for n in range(d/3,d/2+1):
        f = gcd(n,d)
        if f == 1:
            if float(n)/d > 1.0/3:
                ans+=1
print ans
print str(time.clock()*1000)+"ms"
