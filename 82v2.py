f = open("matrix.txt","r")
matrix = [[int(n) for n in s.split(',')] for s in f.readlines()]
m = len(matrix)		
n = len(matrix[0])	
paths = [[0 for i in xrange(n)] for i in xrange(m)]

for i in xrange(0, m):
	paths[i][0] = matrix[i][0]

for col in xrange(1, n):
	for row in xrange(0, m):
		paths[row][col] = paths[row][col-1] + matrix[row][col]
	for dc in xrange(1, m):
		paths[dc][col] = min(paths[dc][col], paths[dc-1][col] + matrix[dc][col])
		paths[-dc-1][col] = min(paths[-dc-1][col], paths[-dc][col] + matrix[-dc-1][col])

print min([l[-1] for l in paths])
