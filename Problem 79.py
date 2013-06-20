f = open('keylog.txt','r')
attempts = [int(line) for line in f]

rank = []
for x in attempts:
    rank.append((x/100,0))
    rank.append((x/10%10,1))
    rank.append((x%10,2))

rank.sort()
c = ''
for x in attempts:
    c += str(x)
c = list(set(c))
    
    
b = []
for x in c:
    a = 0
    for y in rank:
        if y[0] == int(x):
            a += y[1]

    b.append((a,x))
b.sort()
ans = ''
for x in b:
    ans += str(x[1])
print b
print ans

