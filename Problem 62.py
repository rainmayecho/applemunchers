import itertools

    

cubes = [4642**3]
x = 4642
while len(str(cubes[-1]))== 12:
    x+=1
    cubes.append(x**3)

print len(cubes)

poss = []
for x in cubes:
    poss.append(x)
    for y in cubes:
        if not len(str(y))== len(str(x)):
            continue
        if not y == x:
            a = list(str(x))
            a.sort()
            b = list(str(y))
            b.sort()
            if a == b:
                poss.append(y)
    if len(poss) == 5:
        print x
        break
    else:
        poss = []
                
    
    
