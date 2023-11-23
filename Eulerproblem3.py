lista=list(range(2,10000))
n=0
while n < int(len(lista)):
    i = 0
    while i+1 < int(len(lista)):
        if int(lista[n]) % int(lista[i]) == 0 and int(lista[n]) != int(lista[i]):
            break
        i = i + 1
    if int(lista[n]) % int(lista[i]) == 0 and int(lista[n]) != int(lista[i]):
        del lista[n]
        n = n-1
    n=n+1
x = 600851475143
for b in range (0, 10):
    if x == 1:
        break
    for z in range(0,int(len(lista))):
        if x % int(lista[z]) == 0:
            x = x / lista[z]
            print(lista[z])
            break
print (x)
