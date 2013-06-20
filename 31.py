currency = [200,100,50,20,10,5,2,1]

def func(r = 200, limit = 200):
    if r == 0:
        return 1
    a = 0
    for i in currency:
        if i <= min(r,limit):
            a += func(r-i,i)
    return a
            
print func()



    

