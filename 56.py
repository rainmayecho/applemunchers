digsum = 0
for a in range(2,101):
    for b in range(2,101):
        temp = sum(int(x) for x in str(a**b))
        if  temp > digsum:
            digsum = temp
print digsum
            
