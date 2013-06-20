from Useful import comb

def npart(n, b):
    while len(b) < n:
        nb = [b[-1]]
        for i in xrange(len(b)):
            nb.append(b[i] + nb[i])
        b = nb    
    return b[-1]

n = 60
m = 40

print npart(n,[1]) / npart(m,[1]) + 1
