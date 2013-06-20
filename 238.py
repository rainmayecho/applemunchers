s0 = 14025256
s = str(s0)
prev = s0
while len(s) < 10**5:
    sn = prev**2 % 20300713
    s += str(sn)
    prev = sn

t_set = range(1,1001)
ps = 0
i = 0
while i < len(s):
    j = i+1
    while j <= len(s):
        ds =  sum([int(n) for n in s[i:j]])
        if ds in t_set:
            ps += i+1
            #print ds, i, j
            t_set.remove(ds)
        j += 1
    if not t_set:
        break
    i += 1
    
    
print ps
