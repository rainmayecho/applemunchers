import random

def pie(x):
    F = 1.0000/x
    result = []
    M = 10**5
    while len(result) <= M:
        count = 0
        cF = 1.00
        while cF >= F:
             chance = (cF-F)/cF
             choice = random.random()
             #print cF, chance, choice
             count += 1
             if choice > chance:
                 break
             cF -= choice
        #print count
        result.append(count)
    return  float(sum(result))/M


print pie(2)       
