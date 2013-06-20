import Useful, time, phi

## takes too long, ~ 28 hrs
def f(n):
    s = 0
    for x in xrange(2,n/2):
        for y in range(1,x):
            if not Useful.gcd(x,y) == 1 and not y == 1:
                continue
            if (x+y)<= (n/2):
                s += n/(x+y)-1
    return s*12 + (n-1)*6 + (n/2-1)*6


## this one is much faster
def h(n):
    s = 0
    for x in xrange(1,n/2+1):
        s += (n/x-1)*phi.totient(x)
    return s*6
        
        
time.clock()
print h(10**8)
print str(time.clock()*1000)+'ms'



              
                  
