# creer une liste qui va stocker des pseudo pour simuler un jeu en ligne

# Dragfy, Graven, Cleymax, ...

online_players = ["Dragfy", "Graven", "Anana", "Cleymax", "Luc"]

print(online_players)
print("modification pseudo")

# modifier 'Graven' -> 'DarkFantasy'
online_players[1] = "DarkFantasy"

# insert un utilisateur après le 4 eme éléments
online_players.insert(4, "Dark")
print(online_players)

# remplacer le 2 et le 4 eme élément
online_players[2:4] = ["Devil", "Alexei"]
print(online_players)

# en ajouter d'autres
#on imagine qu'un joueur "Gameur123" se connecte
online_players.append("Gameur123")
print(online_players)

#ajouter 2 utilisateurs
online_players.extend(["Emilio", "Dayl"])
print(online_players)

#déconnection d'un user
del online_players[6]
print(online_players)
online_players.pop(4)
print(online_players)

#retirer un user par le nom
online_players.remove("DarkFantasy")
print(online_players)

#si on veut supprimer tout la liste
#premiere façon
del online_players[:]
#2eme façon
#online_players.clear()
print(online_players)


