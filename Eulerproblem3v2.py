#Version 2
from decimal import Decimal, getcontext
getcontext().prec= 2**6
#start
factors=list()
from decimal import Decimal, getcontext
def get_primes(n):
    i = int(2)
    eva = 0
    n= int(n)
    raiz = n ** 0.5
    print(n, 0)
    while float(i) < raiz:
        if eva == 0 and Decimal(n) % Decimal(2) == 0:
            n = Decimal(n)//Decimal(2)
            factors.append(int(2))
            print(2)
            get_primes(n)
            return factors
        if Decimal(n) % Decimal((2*i)-1) == 0:
            eva += 1
            n = Decimal(n)//Decimal((2*i)-1)
            print((2*i)-1, 2)
            factors.append(int(2*i-1))
            get_primes(n)
            return factors
        if (2**i)-1 < raiz and Decimal(n) % Decimal((2**i)-1) == 0:
            n = Decimal(n)//Decimal((2**i)-1)
            print((2**i)-1, 3)
            factors.append(int((2**i)-1))
            get_primes(n)
            return factors
        i += 1
    if float(i) >= raiz:
        factors.append(int(n))
        n = Decimal(n//i)
        return factors
#pendent: fer un checker de la llista i els problemes de precisió en les divisions
print(get_primes(2124312424353167))

