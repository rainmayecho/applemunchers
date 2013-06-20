from Useful import comb

def C(n, k):
    t = n
    p =  1
    lim = min(k, n-k)
    while t > lim:
        p *= t
        t -= 1
        
