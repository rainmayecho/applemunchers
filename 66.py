import Useful, time


def pell(d):
    p = 1
    k = 1
    x1 = 1
    y = 0
    sd = d**.5

    while k != 1 or y == 0:
        p = k*(p/k+1)-p
        p = p - int((p-sd)/k)*k

        x = (p*x1+d*y) / abs(k)
        y = (p*y+x1) / abs(k)
        k = (p*p-d) / k

        x1 = x

    return x

time.clock()
print max([(pell(d),d) for d in Useful.get_primes(1000)])
print str(time.clock()*1000)+'ms'
