import itertools, time

time.clock()
digits = [0,1,2,3,4,5,6,7,8,9]
plist = list(itertools.permutations(digits))
print plist[999999]
print str(time.clock()*1000)+"ms"
