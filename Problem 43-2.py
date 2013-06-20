import itertools

def find_next(digit, primes,index, current, answers):
    if current in ans:
        return False
    if len(current) == 10:
        return current
    if not len(set(current)) == len(current):
        return False
    if digit/100 == 0:
        sdigit = '0'+str(digit)
    else:
        sdigit = str(digit)
    c = current
    for x in range(0,10):
        if x in current:
            continue
        a = sdigit[:2]
        b = str(x) + a
        if int(b) % primes[index] == 0:
            c.append(int(b[0]))
            if find_next(int(b),primes,index+1,c, answers):
                return current
    current.pop()
    return False

d17 = []
current = []
primes = [13,11,7,5,3,2,1]
ans = []

for x in range(100,1000):
    if x%17 == 0:
        d17.append(x)
for x in d17:
    current = [int(y) for y in str(x)]
    current.reverse()
    a = find_next(x,primes,0,current,ans)
    if a:
        ans.append(a)
    else:
        continue
    current = []
    current = [int(y) for y in str(x)]
    current.reverse()
    b = find_next(x,primes,0,current,ans)
    if b:
        ans.append(b)
    current = []

print ans
