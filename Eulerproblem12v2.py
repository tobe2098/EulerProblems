
def get_pf(x):
    '''
    Given x : return a list of prime factors
    '''
    factors = set()
    i = 2
    while i <= x:
        if x%i==0:
            factors.add(i)
            x//=i
            continue
        else:
            i+=1
    return list(factors)

def get_exp_of_pf(x):
    '''
    Given x:

        1. get a list of prime factors (sorted)
        2. working backwards, get the exponents for each pf.
        3. keep track of the exponents to calculate total number of factors
        4. return
            bases (i.e. prime factors) as list
            exponents (1 value for each base >= 1) as list
            number of factors as a scalar
    '''
    a,b = [],[]
    nf = 1
    pf = get_pf(x)             # retrieves prime factors
    pf.sort()

    while pf:                  # finds exponents of the prime factors
        base = pf.pop()
        e = 1
        while(x % base**e==0):
            e += 1
        b.append(base)
        a.append(e-1)
        nf *= e
    return(b,a,nf)               # returns two lists bases (b) and exponents (a) and total factors (nf)

def find_triangle_with_n_divisors(n):
    s = 0
    f = 1
    i = 0

    while f<n:
        i += 1
        s += i
        _,_,f = get_exp_of_pf(s)
    return(s)

solution = find_triangle_with_n_divisors(500)
