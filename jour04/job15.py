L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

arrond = [round(num) for num in L] 

for i in range(len(arrond)):
    for j in range(i + 1, len(arrond)):
        if arrond[i] > arrond[j]:
            arrond[i], arrond[j] = arrond[j], arrond[i]

print(arrond)
