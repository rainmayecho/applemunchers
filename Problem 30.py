import time

values = []
for i in range(0,10):
    values.append(i**5)

def analyze(n):
    total = 0
    for x in str(n):
        total += values[int(x)]
    if total == n:
        return True
    else:
        return False
        
def solve():
    ans = []
    for i in range(3125,12**5):
        if analyze(i):
            ans.append(i)
    print sum(ans)
    print ans
                
t1 = time.time()
##time.clock()
solve()
print str((time.time()-t1)*1000)+"ms"
##print str(time.clock()*1000)+"ms"
    
    
    
