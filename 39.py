triplet = []
for a in range(3,300):
    for b in range(4,400):
        c = (a**2+b**2)**.5
        if c == int(c):
            t = [a,b,int(c)]
            t.sort()
            if t not in triplet:
                triplet.append(t)
                

peri = []
for x in triplet:
    peri.append(sum(x))
peri.sort()
print peri
