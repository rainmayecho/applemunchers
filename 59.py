import itertools
import string
import operator
import sys

def xor(a, key):
    return chr(a ^ ord(key))

inp = open('cipher1.txt','r')
inlist = []
for line in inp:
    a = line.split(',')
    for e in a:
        inlist.append(int(e))

alphabet = string.ascii_lowercase
comb = list(itertools.product(alphabet,repeat = 3))

msg = ''
i = 0
flag = False
mkey = ''

for key in comb:
    for char in inlist:
        if i > 2:
            i = 0
        msg +=(xor(char,key[i]))
        i += 1
    if ' the ' in msg:
        flag = True
        mkey = key    
        print msg
    if flag:
        break
    msg = ''

j = 0
s = 0
for x in msg:
    if j > 2:
        j = 0
    s += ord(x)

print s

##string = ''
##for char in inlist:
##    string+= chr(char)
##print string
