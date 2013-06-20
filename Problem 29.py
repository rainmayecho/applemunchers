import time

t1 = time.time()
values = []
for a in range(2,101):
    for b in range(2,101):
        values.append(a**b)
print len(list(set(values)))
print str(int((time.time()-t1)*1000))+"ms"
