import math

def pascal(p, lim):
    if lim == 0:
        return 0
    n = int(math.log(lim,7))
    t = lim/(7**n)
    count = p*28**n*t*(t+1)/2
    lim %= 7**n
    p *= (t+1)
    count += pascal(p,lim)
    return count

print pascal(1,10**9)
