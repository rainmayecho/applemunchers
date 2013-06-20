import math, gmpy

def check(a,b,p):
    semip = p/2
    c = (semip*(semip-b))
    if gmpy.is_square(c):
        print (a,a,b,p)
        return True
    return False

psum = 0
for s in xrange(5,333333334,2):
    p = 3*s+1
    if check(s,s+1,p):
        psum+=p
    p = 3*s-1
    if check(s,s-1,p):
        psum+=p
        
print psum

