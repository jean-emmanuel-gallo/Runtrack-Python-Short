def dessiner_tapis(n):
    for i in range(n+1):
        for j in range(n+1):
            if i == j:
                print("x", end="")
            else:
                print("-", end="")
        print()

print(dessiner_tapis(11))