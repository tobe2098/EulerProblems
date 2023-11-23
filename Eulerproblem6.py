S1 = 0
S2 = 0
for i in range(1,101):
    S1 = i + S1
S1 = S1 * S1
for c in range(1,101):
    S2 = (c * c) + S2
print(S1)
print(S2)
print(S1-S2)
