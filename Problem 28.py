import time

time.clock()
total = 0
for x in range(0,501):
    if x == 0:
        total += 1
    else:
        n = 2*x
        m = (2*x+1)**2
        total += 4*m-6*n
print total
print str(time.clock()*1000)+"ms"
    
        
    
