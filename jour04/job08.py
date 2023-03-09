L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91] 

sommes_val_paires = 0
for i in L:
    if i % 2 == 0:
        sommes_val_paires += i
print("La somme de toutes les valeurs paires de la liste est :", sommes_val_paires)