def func():
    i=900
    palindrome = 0
    for x in range(i,1000):
        for y in range(i+1,1000):
            if is_palindrome(str(x*y)) and x*y > palindrome:
                palindrome = x*y
    return palindrome



def is_palindrome(input):
    string = list(input)
    string.reverse()
    if list(input) == string:
        return True
    return False
    

    
        
