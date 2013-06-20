
a = [1,2]
b = [2]
while max(a)<4000000:
    a.append(a[len(a)-1]+a[len(a)-2])
    if a[len(a)-1]%2==0:
        b.append(a[len(a)-1])
print sum(b)

        
