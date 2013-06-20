ans = []
for x in range(9000,9500):
    a = str(x)
    i = 2
    while len(str(a)) < 9:
        a += str(x*i)
        i += 1
    b = ''.join(sorted(a))
    if len(b) > 9:
        continue
    if '0' in b:
        continue
    if '123456789' in b:
            ans.append(int(a))
print max(ans)        
    
