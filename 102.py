import math, time

time.clock()

f = open('triangles.txt','r')
coord = [[int(n) for n in s.split(',')] for s in f.readlines()]

def dot(v1,v2):
    return v1[0]*v2[0]+v1[1]*v2[1]

def mag(v):
    return (v[0]**2+v[1]**2)**.5

def contains(v1,v2,v3):
    t1 = (math.acos(dot(v1,v2)/(mag(v1)*mag(v2))))
    t2 = (math.acos(dot(v1,v3)/(mag(v1)*mag(v3))))
    t3 = (math.acos(dot(v2,v3)/(mag(v2)*mag(v3))))
    s = t1+t2+t3
    if s > 6.2831:
        return True
    return False

c = 0
for tri in coord:
    v1 = (tri[0],tri[1])
    v2 = (tri[2],tri[3])
    v3 = (tri[4],tri[5])
    if contains(v1,v2,v3):
        c+=1
print c
print str(time.clock()*1000)+"ms"
        
    
        
