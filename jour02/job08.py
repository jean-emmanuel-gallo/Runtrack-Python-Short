def afficher_fruits(type, saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine, navet")

afficher_fruits("fruits", "hiver") 
afficher_fruits("fruits", "ete") 
afficher_fruits("legume", "hiver")
afficher_fruits("legume", "ete") 


