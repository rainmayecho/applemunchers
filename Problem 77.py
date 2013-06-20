from Useful import get_primes

def prime_partition(n, primes,depth):
    S = []
    N = []
    count = 0
    if n == 0:
        return []
    if n == 1:
        return False
    if n == 2:
        return [2]
    if n == 3:
        return [3]
    for p in primes:
        if p > n:
            break
        S.append(p)
        e = prime_partition(n-p, primes,depth+1)
        if e:
            S.extend(e)
        else:
            S.pop()
        if sum(S) == n and depth == 0:
            S.sort()
            print S
            if S not in N:
                N.append(S)
                count += 1
            S = []
        elif sum(S) == n:
            N.append(S)
            S = []

    if depth == 0:
        return count
    return N


primes = get_primes(100)
print prime_partition(10,primes, 0)
