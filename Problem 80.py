from Useful import digit_sum
from decimal import*

total = 0
iroot = [x for x in range(1,101) if x not in [1,4,9,16,25,36,49,64,81,100]]
for i in iroot:
    getcontext().prec = 102
    a = str(int((Decimal(i)**Decimal(.5))*Decimal(10**99)))[0:]
    total += digit_sum(int(a))

print total

