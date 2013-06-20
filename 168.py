s = 0
for n in xrange(11,10000000):
    if (int(str(n)[-1]+str(n)[:-1]) % n) == 0:
        s += n
        print n
print s

