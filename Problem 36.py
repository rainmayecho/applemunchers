def is_palindrome(input):
    string = list(input)
    string.reverse()
    if list(input) == string:
        return True
    return False

def binary(n):
    s = ''
    while n > 0:
        s = str(n%2)+s
        n/= 2
    return s

total = 0
for x in range(1,1000000):
    if is_palindrome(str(x)):
        b = binary(x)
        if(is_palindrome(b)):
            total+=x
print total
            
