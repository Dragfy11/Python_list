from random import shuffle

#GENERATEUR DE PHRASE

#demander en console une chaine de la forme "mot1/mot2/mot3/mot4/..."
text = input("Entrer une chaine de la forme mot1/mot2/mot3/mot4/...").split("/")
#transfomer cette chaine en une liste
print(text)
#la mélanger
shuffle(text)
print(text)
# nombre d'élément
nbr = len(text)
#si le nombre d'élements de cette liste est inférieur à 10
if nbr < 10:
# -> afficher les deux premiers mots
    print(text[0], text[1])
#si  le nombre d'élements est supérieur ou egal à 10
else:
# -> afficher les 3 derniers
    print(text[-1], text[-2], text[-3])