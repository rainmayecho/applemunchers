## Checks if the input has 9 unique digits
def is_pandigital(a):
    if not len(a) == 9:
        return False
    if a == list('123456789'):
        return True
    else:
        return False

products = []
for i in range(2,9999):
    for j in range(2,9999/i):
        product = i*j
        if len(str(i)+(str(9999/i))+str(i)) < 8:
            break
        a = list(str(product)+str(i)+str(j))
        if len(a) > 9:
            break
        a.sort()
        if is_pandigital(a):
            ## Accounts for duplicate products
            if product not in products:
                products.append(product)
                
print sum(products)

## Runtime ~~ 145 ms --
