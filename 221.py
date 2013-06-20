l = []
for p in range(1,10000):
    for d in range(1, p):
        if not (p**2 +1) % d:
            l.append(p*(p+d)*(p+(p**2+1)/d))

print len(l),       
l.sort()
l = list(set(l))
l.sort()
print len(l),

print l[150000]
