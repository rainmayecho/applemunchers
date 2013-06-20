def p(S):
    p = 1
    for i, x in enumerate(S):
        p *= x**(i+1)
    return p

##Lagrange Multiplier, grad P = (1,1,...1)
## x_i = i*2/(n+1)
def f(n):
    return [i*(2.0/(n+1)) for i in xrange(1, n+1)]

s = 0
for n in xrange(2, 16):
    s += int(p(f(n)))

print s

        
