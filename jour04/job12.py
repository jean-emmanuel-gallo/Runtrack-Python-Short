L = [2, 8, 9, 4, 5, 1, 44, 11, 344]

for i in range(len(L)):
    for j in range(i + 1, len(L)):
        if L[i] > L[j]:
            L[i], L[j] = L[j], L[i]

print(L)