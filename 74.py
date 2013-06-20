import math
def fchain(n):
    s = 0
    while n > 0:
        s+=math.factorial(n%10)
        n/=10
    return s

tot = 0
target = 60
frange = range(1,1000000)
skip = []
for x in frange:
    a = []
    a.append(x)
    a.append(fchain(x))
    b = fchain(a[-1])
    count = 0
    while b not in a:
        a.append(b)
        b = fchain(a[-1])
        count += 1
    if count == target-2:
        tot +=1

print tot
