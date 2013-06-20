for x in range(10,1000000/6):
    s = ''.join(sorted(str(x)))
    flag = False
    for y in range(2,7):
        a = ''.join(sorted(str(x*y)))
        if a == s:
            flag = True
            continue
        else:
            flag = False
            break
    if flag:
        print x
        break
        
        
