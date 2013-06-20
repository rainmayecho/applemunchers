import time
k = {0:'',1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
7:'seven',8: 'eight', 9: 'nine',
10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',
30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy',
80:'eighty', 90:'ninety', 100:'hundred', 1000:'thousand'}
teens = [11,12,13,14,15,16,17,18,19]
word = ''
time.clock()
for x in range(1,1001):
    if x == 1000:
        word+=k[x/1000]+k[1000]
    elif x >= 100:
        if x%100==0:
            word+=k[x/100]+k[100]
        elif x%100 in teens:
            word+=k[x/100]+k[100]+'and'+k[x%100]
        else:
            word+=k[x/100]+k[100]+'and'+k[(x%100)/10*10]+k[x%10]
    elif x > 20:
        word+=k[x/10*10]+k[x%10]
    else:
        word+=k[x]
print len(list(word))
print str(time.clock()*1000)+'ms'



