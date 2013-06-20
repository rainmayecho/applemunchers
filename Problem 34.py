
def check(n):
    a = n
    total = 0

    ## Checks if the argument contains a digit whose
    ## factorial is greater than itself
    ## Probably not necessary

##    if n < k[9]:
##        if '9' in str(n):
##            return False
##    if n < k[8]:
##        if '8' in str(n):
##            return False
##    if n < k[7]:
##        if '7' in str(n):
##            return False
##    if n < k[6]:
##        if '6' in str(n):
##            return False
##    if n < k[5]:
##        if '5' in str(n):
##            return False

    while a > 0:
        total += k[a%10]
        a /= 10
    if total == n:
        return True
    else:
        return False

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

##Dictionary of factorial(0-9) , a = factorial(9), factorial(8) = a/9 ... etc?
k = {0:1, 1:factorial(1), 2:factorial(2) , 3:factorial(3) ,
4:factorial(4) , 5:factorial(5) , 6:factorial(6) , 7: factorial(7) ,
8:factorial(8) , 9:factorial(9)}

## z = k[9]
## for y in range(1,9):
##    z += k[y]*(y-1)
## z = 46234, sufficient upper bound
## lower bound is the given 145 because int < 100
## are restricted to digits containing [4,3,2,1]
## by some inspection, no number would be in this range

numsum = 0
for x in range(145, 46234):
    if check(x):
        numsum += x

print numsum

##Runtime-- 90ms --
        
     
