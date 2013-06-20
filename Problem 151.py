bag = [1,1,1,1]
def solve(bag):
    if sum(bag) == 1:
        if bag[3] == 1:
            return 0.0
        if bag[0] == 1:
            return 1.0 + solve([0,1,1,1])
        if bag[1] == 1:
            return 1.0 + solve([0,0,1,1])
        else:
            return 1.0 + solve([0,0,0,1])
    else:
        den = float(sum(bag))
        r = 0.0
        if bag[0] > 0:
            r += (bag[0]/den) * solve([bag[0]-1, bag[1]+1, bag[2]+1, bag[3]+1]) 
        if bag[1] > 0:
            r += (bag[1]/den) * solve([bag[0], bag[1]-1, bag[2]+1, bag[3]+1])
        if bag[2] > 0:
            r += (bag[2]/den) * solve([bag[0], bag[1], bag[2]-1, bag[3]+1])
        if bag[3] > 0:
            r += (bag[3]/den) * solve([bag[0], bag[1], bag[2], bag[3]-1])
    return r

print '0.'+str(int(solve(bag)*10**6 + 1))
