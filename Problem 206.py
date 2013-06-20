##From wikipedia, 1_2_3_4_5_6_7_8_900 is guaranteed.
##So, the answer has the form 1 _ _ _ _ _ _ _ _ 0
##Also, the answer has the form 1 _ _ _ _ _ _ _ 3 0 or 1 _ _ _ _ _ _ _ 7 0.
## This leaves a brute force of squares of the form 1_2_3_4_5_6_7_8_900
## while only iterating through 19999999 backwards


corr = '1234567890'
for x in xrange(10000000,19999999):
    a = str(int(str(x)+'30')**2)
    b = str(int(str(x)+'70')**2)
    c = a[::2]
    d = b[::2]
    if c==corr:
        print int(a)**.5
        break
    if d==corr:
        print int(b)**.5
        break
