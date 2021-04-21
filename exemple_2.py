# premiere façon
#import statistics pour faire la moyenne
# deuxième façon
from statistics import mean
from random import shuffle

# exemple de note

note = [8, 9, 10, 11, 12, 14]
print(note)

#module : shuffle -> random
shuffle(note)
print(note)

#module : statistics

# Pour pouvoir avoir la moyenne des notes, il suffit de d'importer le module statistics  au début du script et de créer une varible suivi du module statistics
#premiere façon
#result = statistics.mean(note)

#deuxième façon
result = mean(note)

print(" la moyenne de l'élève est de {}".format(result))