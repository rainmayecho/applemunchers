import math

table = []
for x in range(0,12):
    row = []
    for y in range(0,19):
        row.append(3**x*2**y)
    table.append(row)

def wrapper(n):
    i = math.floor(log(3,n))
    j = math.floor(log(2,n))
    


        
