import time

def f(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

##Implements the LaGrange Interpolating function
def lagrange(seq, n):
    s = 0
    for i in xrange(len(seq)):
        p = 1
        for j in xrange(len(seq)):
            if i == j:
                continue
            p *= float(n-j)/(i-j)  
        s += seq[i]*p
    return s

time.clock()
seq = [f(n) for n in xrange(1, 12)]
s = 0 

for i in range(1, len(seq)):
    v = lagrange(seq[:i],i)
    print v, i
    s += lagrange(seq[:i],i)

print int(s)
print str(time.clock()/1000)+'ms'

