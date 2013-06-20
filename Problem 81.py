import time

time.clock()

f = open('matrix1.txt','r')
mat = [[int(n) for n in s.split(',')] for s in f]

size = len(mat)-1

for i in range(size,-1,-1):
    for j in range(size,-1,-1):
        if i==size and j==size:
            continue
        if j==size:
            mincell = mat[i+1][j]
        elif i==size:
            mincell = mat[i][j+1]
        else:
            mincell = min(mat[i+1][j],mat[i][j+1])
        mat[i][j] += mincell

print mat[0][0]
print str(time.clock()*1000)+'ms'

