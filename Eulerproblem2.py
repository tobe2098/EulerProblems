x=0
y=0
z=1
res = 0
while x < 4000000:
    x=y+z
    z=y
    y=x
    if x % 2 == 0:
        res = res + x
print(int(res))
