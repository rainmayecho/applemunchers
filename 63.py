count = 0
for n in range(1,10):
    for p in range(1,3*n):
        t = n**p/10**(p-1)
        if t >= 1 and t < 10:
            count += 1
print count
