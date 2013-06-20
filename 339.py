import random

def bleat(w,b,truth):
    bl = random.randint(0,1)
    if bl:
        truth.append(True)
        w += 1
        b -= 1
    else:
        truth.append(False)
        b += 1
        w -= 1
    if w > b:
        w = 0
        return (w,b,truth)
    if True in truth:
        w = 0
        return (w,b,truth)

    return (w,b,truth)

def func():
    total = 0
    truth = []
    for x in range(1,11):
        done = False
        w = 5
        b = 5
        while not done:
            a = bleat(w,b)
            w = a[0]
            b = a[1]
            if w == 0:
                done = True
        total += b

    total /= 10.0
    return total

print func()


##    if b > w:
##        if b-w > 10:
##            w = 0
##            return (w,b)
##        elif b-w > 8:
##            return (w,b)
##        elif b-w > 6:
##            return (w,b)
##        elif b-w > 4:
##            return (w,b)
##        elif b-w > 2:
##            w -= 1
##            return (w,b)
##    if w == b:
##        w -= 1
##        return (w,b)
