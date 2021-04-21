#pour mettre chaine de mot dans un tableau il suffit de mettre un split et mettre d'où l'on veut le sélectionner

text = input("Entrer une chaine de la forme (email-pseudo-motdepasse)").split("-")
print(text)

print("Bonjour {}, votre mail est '{}', votre mot de passe est '{}'".format(text[1], text[0], text[2]))