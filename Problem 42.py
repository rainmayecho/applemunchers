import string, itertools, time

time.clock()
inp = open('words.txt','r')
for line in inp:
    w = line.split(',')

words = []
for word in w:
    words.append(word.lower())

k = dict((x,i+1) for i, x in enumerate(string.ascii_lowercase))
d = {'"':0, ',':0}
k.update(d)

triangle = [.5*x*(x+1) for x in range(1,20)]

count = 0
for word in words:
    value = sum(k[char] for char in list(word))
    if value in triangle:
        count += 1

inp.close()
print count
print str(time.clock()*1000)+"ms"
    
    



