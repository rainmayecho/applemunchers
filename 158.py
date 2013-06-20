def p(n,k,l, flag, used):
    if l == 1:
        return 1
##  word is 1 letter from completion, but hasn't had
##  an instance occur, so forces the instance to occur.
    if l == 2 and not flag:
        for j in xrange(k+1, 27):
            if j in used:
                continue
            used.append(j)
            k += p(n, j, l-1,True, used)
            used.pop()
        return k

    
    if flag:
##      Since the one instance has occurred, only recurse on
##      letters < current letter, else recurse both types.
        for j in xrange(1, k):
            if j in used:
                continue 
            used.append(j)
            k += p(n, j, l-1, True, used)
            used.pop()
    else:
##      Iterate through letters < current letter
        for j in xrange(1, k):
            if j in used:
                continue
            used.append(j)
            k += p(n, j, l-1, False, used)
            used.pop()
##      Iterate through letters > current letter
        for j in xrange(k+1, 27):
            if j in used:
                continue
            used.append(j)
            k += p(n, j, l-1,True, used)
            used.pop()

    return k

n = 3
s = 0
for k in xrange(1,27):
    s += p(n,k,n,False, [k])
    
print s
