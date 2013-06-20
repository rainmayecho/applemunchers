import time
time.clock()
file = open("Problem13.txt","r")
num = [line for line in file]
nlist = map(lambda x: long(x), num)
print repr(sum(nlist))[0:10]
print str(time.clock()*1000)+" ms"



