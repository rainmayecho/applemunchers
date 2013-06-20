import itertools,time

time.clock()

rsol = []
for x in range(1,400):
    for y in range(1,400):
        rsol.append(((x**2+x)*(y**2+y)/4,x,y))

mindiff = 2000000
ans = 0
for z in rsol:
    d = 2000000-z[0]
    if d < mindiff and d > 0:
        mindiff = d
        ans = z[1]*z[2]
print ans
print str(time.clock()*1000)+"ms"   
        
    
