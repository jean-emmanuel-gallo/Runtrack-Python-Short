L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Valeur de L[1]:", L[1])

def remplacer_cases_voisines(L):
    L[3] = L[2] + L[4]

remplacer_cases_voisines(L)

print("Dernière valeur de la liste L:", L[-1])