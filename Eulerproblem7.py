lista=list(range(2,3))
print(lista)
i = 2
while len(lista) < 10001:
    n = 0
    eva = 0
    while int(lista[n]) < i:
        if i % int(lista[n]) == 0:
            break
        else:
            eva = eva + 1
            if eva == int(len(lista)):
                lista.append(i)
        n = n + 1
    i = i + 1
print(lista[10000])
