from Useful import gcd
import math

##unsure of how to finish
L = 1500
G = []
sl = int(L**.5)
count = 0
for m in range(2,sl,1):
    for n in range(1, m,1):
        if not (m - n) % 2:
            continue
        if gcd(m,n) == 1:
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            p = a+b+c
            for k in range(1, L/p ):
                if k*p not in G:
                    G.append(k*p)
                    count += 1
                else:
                    count -=1
print count
