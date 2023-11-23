Lista=list(range(100,999))
Lista2=list()
Lista3=list()
for w in range (0,899):
     for y in range (0,899):
         Lista2.append(int(Lista[w])*int(Lista[y]))
for r in range(0,int(len(Lista2))-1):
    x = int(Lista2[r])
    b = 0
    n = 0
    ff = 0
    while x >= 1:
        x = x / 10
        b = b + 1
    x = str(Lista2[r])
    while n < b:
        m = b - n - 1
        if x[n] == x[m]:
            ff = ff + 1
        n = n+1
    if ff == b:
        Lista3.append(int(Lista2[r]))
print(max(Lista3))
