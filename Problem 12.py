import itertools, operator, time
from Useful import*

def analyze(pfactors):
    pfactors.sort()
    return pfactors
      
def triNum():
    time.clock()
    n = 1
    plist = sieve(12375)
    for x in range(1,19000):
        pfactors = analyze(pfactorize(n,plist,n,[]))
        npfactors = [reduce(operator.mul,j)
                     for i in range(2,len(pfactors)+1)
                     for j in itertools.combinations(pfactors,i)]
        if len(set(npfactors))>500:
            return pfactors
        n += x+1
a = triNum()
print a
p = 1
for x in a:
    p*=x
print p
print str(time.clock()*1000)+"ms"

