for a in range(0,1001):
    b = 1000
    while b > a:
        c = 1000
        while c > b:
            if a + b +c == 1000:
                if a**2 + b**2 == c**2:
                    print (a*b*c)
            c -= 1
        b -= 1
