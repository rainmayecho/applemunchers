
##Simple primality
def is_prime(n):
    if not n % 2:
        return False
    if not n % 3:
        return False
    if not n % 5:
        return False
    for m in xrange(6,int(n**.5)+1, 6):
        if not n % (m+1):
            return False
        if not n % (m-1):
            return False
    return True

##Computes the simple digit sum of a number
def digit_sum(a):
    b = [int(e) for e in str(a)]
    return sum(b)

##Greatest Common Divisor
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

##Least Common Multiple
def lcm(a,b):
    return (a*b)/gcd(a,b)

##Adds two fraction tuples, in reduced form (I think)
def addfrac(a,b):
    if a[1] == b[1]:
        return (a[0]+b[0],a[1])
    m = lcm(a[1],b[1])
    if a[1] == m:
        b = (b[0]*m,b[1]*m)
        return addfrac(a,b)
    if b[1] == m:
        a = (a[0]*m,a[1]*m)
        return addfrac(a,b)
    else:
        a = (a[0]*m,a[1]*m) 
        b = (b[0]*m,b[1]*m)
    return addfrac(a,b)

##Inverse of a fraction//reduces clutter
def inv(f):
    return (f[1],f[0])

##Quite fast prime sieve
def sieve(n):
    sieve = range(n+1)
    sieve[1] = 0
    for i in range(2, int(n**.5)+1):
        if sieve[i]:
           m = n/i - i
           sieve[i*i: n+1:i] = [0] * (m+1)
    return [x for x in sieve if x]

##Pretty fast prime sieve
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

##Prime factorization of a;
##a = argument, supply primes,
##b=a but is static,and pfactors is always initialized as []
def pfactorize(a,primes,b,pfactors = []):
    if a==1:
        return pfactors
    if a==2:
        pfactors.append(2)
        return pfactors
    if a==3:
        pfactors.append(3)
        return pfactors
    for x in primes:
        if a%x==0:
            pfactors.append(x)
    prod = 1
    for y in pfactors:
        prod *= y
    if not prod == b:
        pfactorize(b/prod,primes,b,pfactors)
    return pfactors

##Euler's Totient function
def phi(n, primes):
    if n in primes:
        return n-1
    c = 1
    if n%2==0:
        for x in range(3,n,2):
            if gcd(x,n)==1:
                c+=1
    else:
        for x in range(2,n):
            if gcd(x,n)==1:
                c+=1
    return c

def is_tri(x):
    n = (-1+(8*x+1)**.5)/2
    if n == int(n):
        return True
    return False

def is_square(x):
    n = x**.5
    if n == int(n):
        return True
    return False

def is_pent(x):
    n = ((24*x+1)**.5+1)/6.0
    if n == int(n):
        return True
    return False
    
def is_hex(x):
    n = ((8*x+1)**.5+1)/4
    if n == int(n):
        return True
    return False

def is_hept(x):
    if is_tri(5*x+1):
        return True
    return False

def tri(n):
    return n*(n+1)/2

def square(n):
    return n**2

def pent(n):
    return (3*n**2-n)/2

def hexa(n):
    return n*(2*n-1)

def hept(n):
    return n*(5*n-3)/2

def octa(n):
    return n*(3*n-2)

def digital(n):
    if not n % 9:
        return 9
    else:
        return n % 9

def comb(n, k):
  nt = 1
  for t in range(min(k, n-k)):
    nt = nt*(n-t)//(t+1)
  return nt


def ext_gcd(a,b):
    x = 0
    prevx = 1
    y = 1
    prevy = 0 
    while b:
        q = a/b
        a, b = b, a % b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
    return prevx, prevy, a
