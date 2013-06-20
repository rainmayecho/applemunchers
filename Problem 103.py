n6 = [11,18,19,20,22,25]

A = [20]
t = [20 + x for x in n6]
A.extend(t)
s = ''
for c in A:
    s += str(c)

print s
