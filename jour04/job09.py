L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

min = L[0]
max = L[0]

for i in L:
    if i < min:
        min = i
    if i > max:
        max = i

print("le plus petit nombre de cette liste est :", min)
print("le plus grand nombre de cette liste est :", max)