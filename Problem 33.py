values = []
for n in range(10,100):
    if not n%10 == 0:
        values.append(n)
        
def is_curious(n,d):
    a = common(n,d)
    if float(n)/d == float(a[0])/a[1] :
        return a
    else:
        return [0,0]

def common(n,d):
    a = list(str(n))
    b = list(str(d))
    if a[0] == a[1]:
        if b[0] == b[1]:
            return [1,1]
    for x in a:
        if x in b:
            a.remove(x)
            b.remove(x)
            return [int(a[0]),int(b[0])]
    return [1,1]

frac = [1,1]
for n in values:
    for d in range(n+1,100):
        if d not in values:
            continue
        a = is_curious(n,d)
        if sum(a) > 0:
            frac[0]*=n
            frac[1]*=d
print float(frac[0])/frac[1]        
            
            
    
    
        
