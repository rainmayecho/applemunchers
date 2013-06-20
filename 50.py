def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

primes = get_primes(999000)

maxsum = 0
maxcount = 0

for i in range(0,4):
    s = 0
    count = 0
    fail = 0
    for j in primes[i:600]:
        s += j
        count += 1
        if s in primes:
            if s > 1000000:
                break
            if s > maxsum and count > maxcount:
                maxsum = s
                maxcount = count
        if count < maxcount:
            fail += 1
        if fail > 10:
            break
        else:
            fail = 0
    if fail > 10:
        break

print maxsum
