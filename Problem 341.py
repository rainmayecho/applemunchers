from decimal import*
import math
import time

## Works, but is slow for summation/ large inputs

def golomb(n):
    seq_n = [1]
    g_n = [1]
    while len(g_n) < n:
        seq_n.append(seq_n[-1]+1)
        g_n.append(seq_n[-1])
        s = g_n[seq_n.index(seq_n[-1])]
        for x in range(0,s-1):
            g_n.append(g_n[-1])
    return g_n[-1]


## Also works, but not memory efficient (at most n = 10**8)
def g(n):
    g_n = [1,2,2]
    i = 3
    s = [1,3,5]
    sp = [1,5,11]
    while len(g_n) < n:
        g_n.extend([i]*g_n[i-1])
        a = g_n[i]
        s.append(s[i-1]+a)
        sp.append(sp[i-1]+((i+1)*a))
        i+=1
    return [g_n,s,sp]

def search(sp,n):
    diff = [n-1]
    flag = False
    for e in sp[1:]:
        diff.append(abs(e-n))
        if diff[-1] >= diff[-2]:
            flag = True
            break
    if flag:
        l = len(diff)-1
    else:
        l = len(diff)
    a = [diff[-2],diff[-1],len(diff)]
    return a
        

time.clock()
f = g(10**7)
g = f[0]
s = f[1]
sp = f[2]

ans = 0
for n in range(1,10):
    r = search(sp,n)
    ans = s[r[0]-1]+math.ceil(float(r[0])/(r[2]+1))
    print ans ,r

print int(ans)

print time.clock()

##cubes = [n**3 for n in range(1,100)]
##print sum([g2(10**6)[e-1] for e in cubes])




























##def a(m):
##    if m==0:
##        return 0
##    if m==1:
##        return 1
##    return a(m-1)+g(m)
##    
##def b(m):
##    if m==0:
##        return 0
##    if m==1:
##        return 1
##    return b(m-1)+m*g(m)
##    
##def c(m):
##    if m==0:
##        return 0
##    if m==1:
##        return 1
##    return c(m-1)+m*g(a(m)-(g(m)-1)/2)
##
##def cc(m,k):
##    if k == 0:
##        return c(m)
##    return cc(m,k-1)+(m+1)*(a(m)+k)
##
##def golomb(n,m,k):
##    return b(m)+k*(m+1)+int((n-cc(m,k)+a(m)+k)/(a(m)+k+1))




##k = 0.00204911504257
##k*n**(phi-1)/math.log10(n


##G[(10^6-1)^3] == 160113493649
##
##G[(10^5-1)^3] == 2240166964
##+k*n**(phi-1)/math.log(n))
