from phi import totient

d = 10**6
s = 0
while d > 1:
    s += totient(d)
    d -= 1

print s
