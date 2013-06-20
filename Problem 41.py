import itertools

def is_prime(a):
    for x in range(2,int(a**.5+1)):
        if a%x==0:
            return False
    else:
        return True

poss = [''.join(item) for item in itertools.permutations('1234567',7)]
ans = [x for x in poss if is_prime(int(x))]
print max(ans)
        
