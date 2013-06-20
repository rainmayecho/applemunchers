import math, time
def funct():
    a = 4
    b = 5
    c = 0
    for x in range(a,400):
        for y in range(a+1,401):
            if (x*x+y*y)**.5 == math.trunc((x*x+y*y)**.5):
                a = x
                b = y
                c = (x*x+y*y)**.5
            if a+b+c == 1000:
                return int((a*b*c))
time.clock()
print funct()
print str(time.clock()*1000)+"ms"

