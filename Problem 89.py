from itertools import izip, count
f = open('roman.txt')
inp = [line for line in f]

initial_total = sum([len(e) for e in inp])
for i in range(len(inp)):
    inp[i]= inp[i].replace("DCCCC", "CM")
    inp[i]= inp[i].replace("LXXXX", "XC")
    inp[i]= inp[i].replace("VIIII" , "IX")
    inp[i]= inp[i].replace("IIII" , "IV")
    inp[i]= inp[i].replace("XXXX", "XL")
    inp[i]= inp[i].replace("CCCC" , "CD")
new_total = sum([len(e) for e in inp])
print initial_total - new_total
f.close()
