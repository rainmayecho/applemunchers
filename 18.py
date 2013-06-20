import time, antigravity
time.clock()
tri = [[int(n) for n in s.split()] for s in open('Problem18.txt').readlines()]
for row in range(len(tri)-1, 0, -1):
  for col in range(0, row):
    tri[row-1][col] += max(tri[row][col], tri[row][col+1])
 
print tri[0][0]
print str(time.clock()*1000)+'ms'


        

