from Useful import *
from itertools import izip, count

def prep(l):
    i = 0
    while True:
        if l[i] < 1000 or (l[i]/10) % 10 == 0:
            l.pop(i)
        else:
            i += 1

        if i == len(l)-1:
            break
    return l

def create_sets(n, multi, S, temp):
    if len(S) == 5:
        for fig in multi:
            for e in fig:
                s = int(str(S[-1]%100)+ str(S[0]/100))
                if e == s:
                    S.append(e)
                    print S
                    print sum(S)
                    return S
    for i in range(len(multi)):
        for j in range(len(multi[i])):
            e = multi[i][j]
            if n % 100 == e/100:
                S.append(e)
                copy = [[k for k in l] for l in multi]
                temp = copy.pop(i)
                temp.pop(j)
                return create_sets(e, copy, S,temp)

    return False
    
        

triangle = prep([tri(n) for n in xrange(1,141)])
square = prep([square(n) for n in xrange(1,100)])
pent =prep([pent(n) for n in xrange(1,82)])
hexa = prep([hexa(n) for n in range(1,71)])
hept = prep([hept(n) for n in range(1,64)])
octa = prep([octa(n) for n in range(1,55)])

multi = [hexa,pent,triangle, square, hept]
for e in octa:
    S = [e]
    create_sets(e, multi, S,[0])
        
