import string, itertools, time

time.clock()
names = open('names.txt','r')
for line in names:
    namelist = line.split(',')
namelist.sort()
namelist1 = []
for name in namelist:
    namelist1.append(name.lower())

k = dict((x,i+1) for i, x in enumerate(string.ascii_lowercase))
d = {'"':0, ',':0}
k.update(d)
i = 1
total = 0
for x in namelist1:
    nscore = 0
    for char in list(x):
        nscore+=k[char]
    total+=nscore*i
    i+=1
print total
print str(time.clock()%1000)+"ms"
names.close()

        
