count = 25*10**6
sqr = [x*x for x in xrange(1,25000000)]

for i in xrange(2,len(sqr)):
    for j in xrange(2,len(sqr)):
        if sqr[i] + sqr[j] -1 in sqr:
            count +=1
            print i, j
            break
print count
