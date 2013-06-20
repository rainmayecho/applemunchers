import itertools
mat = [[int(n) for n in s.split()] for s in open('p345.txt').readlines()]

hsum = []
vsum = []
for i in range(0,15):
    hsum.append(sum(mat[i]))

for j in range(0,15):
    s = 0
    for i in range(0,15):
        s+=mat[i][j]
    vsum.append(s)

join = []
for i in range(0,15):
    a = []
    for j in range(0,15):
        a.append(0)
    join.append(a)


for i in range(0,15):
    for j in range(0,15):
        join[i][j] = (hsum[i]+vsum[j]-mat[i][j])/100

for e in join:
    print e



    
        

        

