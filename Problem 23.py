import itertools, operator, time
def create_primes():
    primes = []
    for x in range(2,20162):
        if is_prime(x):
            primes.append(x)
    return primes
        
def is_prime(a):
    if a==2:
        return True
    if a==3:
        return True
    if a<2:
        return False
    if a==5:
        return True
    if a==7:
        return True
    for x in range(2,int(a**.5+1)):
        if a%x==0:
            return False
    else:
        return True

def pfactorize(a,primes,b,pfactors = []):
    if a==1:
        return pfactors
    if a==2:
        pfactors.append(2)
        return pfactors
    if a==3:
        pfactors.append(3)
        return pfactors
    for x in primes:
        if a%x==0:
            pfactors.append(x)
        if x > a:
            break
    prod = 1
    for y in pfactors:
        prod *= y
    if not prod == b:
        pfactorize(b/prod,primes,b,pfactors)
    return pfactors

def analyze(pfactors):
    pfactors.sort()
    return pfactors

def is_abundant(n,plist,abundlist):
    pfactors = analyze(pfactorize(n,plist,n,[1]))
    if is_prime(n):
        return False
    for num in abundlist:
        if n%num == 0:
            return True
    npfactors = list(set([reduce(operator.mul,j)
                for i in range(2,len(pfactors)+1)
                for j in itertools.combinations(pfactors,i)]))
    npfactors.remove(n)
    if sum(npfactors)>n:
        return True
    else:
        return False

##t1 = time.time()
time.clock()
plist = create_primes()
abundlist =[]
oddabund = []
totalrange = range(1,20162)
evenrange = [i for i in range(48,20162) if i%2==0]
oddrange = [i for i in range(48,20162) if not i%2==0]
for x in range(12,20162):
    if is_abundant(x,plist,abundlist):
        abundlist.append(x)
        abundlist.append(x)
small = abundlist[0:8]
sc = list(itertools.combinations(small,2))
smallcomb = list(set([sum(i) for i in sc]))
for n in smallcomb:
    totalrange.remove(n)
for y in abundlist:
    if not y%2 == 0:
        oddabund.append(y)

codd = []
for e in oddabund:
    for d in list(set(abundlist)):
        if not (e+d)%2==0:
            codd.append(e+d)
codd = list(set(codd))

oddrange = [k for k in oddrange if k not in codd]
print sum(totalrange[0:39])+sum(oddrange)
##print str((time.time()-t1)*1000)+"ms"
print str(time.clock())+"s"

#4179871
    
    
