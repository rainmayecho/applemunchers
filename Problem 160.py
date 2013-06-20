import math
import Useful

n = 10**12
lim = math.log(n, 5)
m = 0
for i in range(1, int(lim + 2)):
    m += n/(5**i)

k = m + 5
