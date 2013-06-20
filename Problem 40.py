s = ''
ans = 1
for x in range(1,1000000/5):
    s += str(x)

for x in range(1,7):
    ans *= int(s[10**x-1])
print ans
    
