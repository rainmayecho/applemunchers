
def is_palindrome(n):
    
    if str(n) == str(n)[::-1]:
        return True
    return False

def reverse_add(n):
    a = str(n)
    b = a[::-1]
    return int(a)+int(b)

def is_lychrel(n):
    truth = []
    c = reverse_add(n)
    while len(truth) < 50:
        truth.append(is_palindrome(c))
        c = reverse_add(c)
        if any(truth):
            return False
    return True

count = 0
for n in range(1,10000):
    if is_lychrel(n):
        count += 1
print count
