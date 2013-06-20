def sq_dsum(a, dsum = 0):
    dsum += (a%10)**2
    if a > 0:
        return sq_dsum(a/10,dsum)
    return dsum

count = 0
for x in range(1,1000000):
    if count > int(.16*10000000):
        break
    n = x
    while True:
        n = sq_dsum(n)
        if n == 1:
            count +=1
            break
        if n == 89:
            break

print 1000001-count
            
