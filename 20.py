import time

def digit_sum(a,dsum = 0):
    dsum=dsum+a%10
    if a > 0:
        digit_sum(a/10,dsum)
    else:
        print dsum
time.clock()
a = 1
for x in range(1,101):
    a*=x
digit_sum(a)
print time.clock()










