import time

def bfs(matrix):
    size = len(matrix)
    orig = [[matrix[x][y] for y in range(size)] for x in range(size)]
    print orig
    q = []
    q.append((0,0))
    visited = [[False for x in xrange(size)] for y in xrange(size)]
    while True:
        row = q[0][0]
        col = q[0][1]
        visited[row][col] = True
        del q[0]
        if row > 0:
            val = matrix[row - 1][col] + matrix[row][col]
            if not visited[row -1][col]:
                val = orig[row - 1][col] + matrix[row][col]
                matrix[row - 1][col] = val
                ##visited[row-1][col] = True
                q.append((row-1,col))
            elif val < matrix[row - 1][col]:
                matrix[row - 1][col] = val
                #q.append((row-1,col))
        if col > 0:
            val = matrix[row][col-1] + matrix[row][col]
            if not visited[row][col-1]:
                val = orig[row][col-1] + matrix[row][col]
                matrix[row][col-1] = val
                #visited[row][col-1] = True
                q.append((row,col-1))
            elif val < matrix[row][col-1]:
                matrix[row][col-1] = val
                #q.append((row,col-1))
        if col < size-1:
            val = matrix[row][col+1] + matrix[row][col]
            if not visited[row][col+1]:
                val = orig[row][col+1] + matrix[row][col]
                matrix[row][col+1] = val
                #visited[row][col+1] = True
                q.append((row,col+1))
            elif val < matrix[row][col+1]:
                matrix[row][col+1] = val
                #q.append((row,col+1))
        if row < size-1:
            val = matrix[row+1][col] + matrix[row][col]
            if not visited[row+1][col]:
                val = orig[row+1][col] + matrix[row][col]
                matrix[row][col] = val
                #visited[row + 1][col] = True
                q.append((row+1,col))
            elif val < matrix[row+1][col]:
                matrix[row+1][col] = val
                #q.append((row+1,col))
        if row == size-1 and col == size-1:
            print matrix
            return matrix[row][col]


f = open('83test.txt', 'r')

matrix = [[int(n) for n in s.split(',')] for s in f]
diagonals = []
size = len(matrix)
print bfs(matrix)

