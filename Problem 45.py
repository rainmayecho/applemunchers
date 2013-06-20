tri = [(n*n+n)/2 for n in range(10000,120000)]

def is_pent(x):
    n = ((24*x+1)**.5+1)/6.0
    if n == int(n):
        return True
    return False
    
def is_hex(x):
    n = ((8*x+1)**.5+1)/4
    if n == int(n):
        return True
    return False
    
for x in tri:
    if is_pent(x):
        print x

        
