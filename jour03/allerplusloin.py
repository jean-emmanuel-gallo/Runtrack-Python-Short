#J'ai fais cette exercice via la méthode ".join" et "reversed()""

#Ici je définis une variable, ayant pour nom "name" et pour donnée "Dracula"
name = "dracula" 

#Je redéfinis une deuxième variable, ayant pour nom "name2". Je mets la méthode ".join" afin de séparer les lettres. 
# Ce qui veut dire que dracula n'est plus "dracula" mais "d" "r" "a" "c" "u" "l" "a"
#Et ensuite, j'utilise la méthode reverse pour que "d" "r" "a" "c" "u" "l" "a"   devienne "a" "l" "u" "c" "a" "r" "d"
name2 = "".join(reversed("dracula"))

print(name2)

#Je n'ai pas réussi à le faire via la méthode des boucles. 