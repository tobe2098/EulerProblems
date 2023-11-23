Lista=list()
for n in range(0,1000):
    if n % 3 == 0 or n % 5 == 0:
        Lista.append(n)
        print(sum(Lista))
        print(n)
    else:
        continue
print(sum(Lista))
