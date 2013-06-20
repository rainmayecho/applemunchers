
def comb(n,r):
    s = n-r
    for x in range(2,n):
        n *= x
    for x in range(2,r):
        r *= x
    for x in range(2,s):
        s *= x
    return n/(r*s)


count = 0
for n in range(23,101):
    for r in range(2,n):
        if comb(n,r) > 10**6:
            count += 1
print count
