import time

def is_prime(a):
    if a % 2 == 0:
        return False
    for x in range(3,int(a**.5+1),2):
        if a%x==0:
            return False
    else:
        return True

time.clock()
corners = 1
prev = 1
primediag = 0
for s in range(3,100000,2):
    for x in range(1,5):
        y = prev+(s-1)
        prev = y
        if is_prime(y):
            primediag += 1
    corners += 4
    ratio = float(primediag)/corners
    if ratio < .10:
        print s
        break

print str(time.clock())+" s"
