def is_bouncy(n):
    a = list(str(n))
    b = list(a)
    b.sort()
    if a == b:
        return False
    b.reverse()
    if a == b:
        return False
    return True          

ratio = 0.0
bouncy = 0
total = 0
while not ratio == .99:
    total +=1
    if is_bouncy(total):
        bouncy+=1
    ratio = float(bouncy)/total

print total
    
