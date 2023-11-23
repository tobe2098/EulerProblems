from decimal import Decimal, getcontext
getcontext().prec= 2*12
#start
from decimal import Decimal, getcontext
factors=list()
def get_primes(n):
    i = int(2)
    eva = 0
    n= int(n)
    raiz = n ** 0.5
    while float(i) < raiz:
        if eva == 0 and Decimal(n) % Decimal(2) == 0:
            n = Decimal(n)//Decimal(2)
            factors.append(int(2))
            get_primes(n)
            return factors
        if Decimal(n) % Decimal((2*i)-1) == 0:
            eva += 1
            n = Decimal(n)//Decimal((2*i)-1)
            factors.append(int(2*i-1))
            get_primes(n)
            return factors
        if (2**i)-1 < raiz and Decimal(n) % Decimal((2**i)-1) == 0:
            n = Decimal(n)//Decimal((2**i)-1)
            factors.append(int((2**i)-1))
            get_primes(n)
            return factors
        i += 1
    if float(i) >= raiz:
        factors.append(int(n))
        n = Decimal(n//i)
        return factors
def finddivisors(n):
    checked=list()
    product=list()
    x=get_primes(n)
    for i in x:
        if i in checked:
            continue
        if i not in checked:
            checked.append(i)
        b=1
        for a in x:
            if i == a:
                b += 1
        product.append(b)
    result= 1
    for c in product:
        result *= c
    return result
def finddivisors2(n):
    eval = 0
    for q in range (1,n+1):
        if Decimal(n) % Decimal(q) == 0:
            eval +=1
    return eval
def trianglenumber(n):
    tnumber = int(n*(n+1)/2)
    return tnumber
eva = 0
#224 lower bound
b = 1
while eva == 0:
    factors=list()
    if finddivisors(trianglenumber(b)) > 500:
        print(b)
        factors=list()
        print (trianglenumber(b))
        print (finddivisors(trianglenumber(b)))
        eva+=1
        break
    b += 1
