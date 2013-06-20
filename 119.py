import math

base = 1
exp = 1
M = []
while len(M) < 30:
    n = base**exp
    while math.log(n,10)*9 < base:
        exp += 1
