initialValue = 65
for i in range(0, 6):
    for j in range(0, i + 1):
         alphabate = chr(initialValue)
         print(f"{alphabate}", end="")
         initialValue += 1
    print("")