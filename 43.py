import itertools

def find_next(d, p, i,n):
    a = d
    b = a[:2]
    if len(a)== 9:
        c = int(a)
        return c
    for x in range(0,10):
        if x in n:
            continue
        c = str(x)+b
        f = str(x)+a
        e = set(f)
        if len(list(f)) == len(list(e)):
            if int(c)%p[i] == 0:
                return find_next(f,p,i+1,n)
    n.append(int(a[0]))
    return find_next(a[1:],p,i-2,n)
    
d17 = []
p = [13,11,7,5,3,2,1]
ans = []
##for x in range(100,1000):
##    if x%17 == 0:
##        a = str(x)
##        b = set(a)
##        if len(list(a)) == len(list(b)):
##            d17.append(x)

print find_next(289,p,0,[])


            
            

