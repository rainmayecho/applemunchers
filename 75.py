from Useful import gcd
import math

L = 1500000
G = [0]*L
for m in range(1,int(L**.5),2):
    for n in range(2,int(L**.5)-m,2):
        if gcd(m,n) == 1:
            p = abs(n*n-m*m) + 2*m*n + n*n + m*m
            for s in range(p, L, p):
                G[s] += 1
print G.count(1)
