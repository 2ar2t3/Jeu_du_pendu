import random

Nom_fichier = input("Veuillez entrer le nom du fichier contenant la liste de mots (avec l'extension): ")

Liste_mots = open(f'{Nom_fichier}', 'r').read().split()

Mot_a_trouver = Liste_mots[random.randint(0, len(Liste_mots) - 1)]