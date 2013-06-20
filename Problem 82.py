f = open('p82.txt','r')
inp = [[int(n) for n in s.split(',')] for s in f.readlines()]


def minimize(col, i, size):
    newcol = []
    if i == size-1:
        for j in range(size):
            val = col[i][j]
            newcol.append(col[i-1][j] + val)
        return newcol
    val = col[i][0]
    newcol.append(min(col[i-1][0] + val, col[i-1][1] + col[i][1] + val))
    for j in range(1, len(col)-1):
        val = col[i][j]
        newcol.append(min(col[i-1][j] + val, col[i-1][j+1] + col[i][j+1] + val, col[i-1][j-1] + col[i][j-1] + val))
    size = len(col)-1
    val = col[i][size]
    newcol.append(min(col[i-1][size] + val, col[i-1][size-1] + col[i][size-1] + val))
    return newcol

columns = []
for i in range(len(inp)):
    c = []
    for rows in inp:
        c.append(rows[i])
    columns.append(c)

size = len(columns)
print max(columns[size-1])
for i in range(1,size):
    columns[i] = minimize(columns,i, size)



print min(columns[size-1])
               
print columns[-1]        
        
    
            
