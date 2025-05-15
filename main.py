import random

#Demande à l'utilisateur si il a un fichier contant une liste de mot ou non, si oui on utilise son fichier, sinon l'original.
"""if input("Avez vous un fichier contenant une liste de mots ? ('oui' ou 'non') : ") == "oui":
    Nom_fichier = input("Veuillez entrer le nom du fichier contenant la liste des mots (avec l'extension): ")
else:"""
Nom_fichier = "Liste_de_mots.txt"

#Ouverture du fichier, lecture et transformation de la chaine de charactères en une liste de mots.
Liste_mots = open(f'{Nom_fichier}', 'r', encoding='utf-8').read().split()

#Choix d'un mot au hasard dans la liste des mots.
Mot_a_trouver = Liste_mots[random.randint(0, len(Liste_mots) - 1)]

#Création de deux chaines de charactères contenant les accents possibles et leurs équivalents.
#Important de bien faire correspondre les indices des accents avec leur équivalent sans accent.
lettres_accentuées = "àâäéèêëîïôöùûüçÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ"
lettres_non_accentuées = "aaaeeeeiioouuucAAAEEEEIIOOUUUC"

#Création d'une variable str vide qui sera le mot sans accent.
mot_normalisé =""

#On itère sur chaque lettre du mot initial.
for lettre in Mot_a_trouver:
    if lettre in lettres_accentuées: #Si une lettre est un accent, on ajoute au mot, son équivalent.
        mot_normalisé += lettres_non_accentuées[lettres_accentuées.find(lettre)] #utilisation de find() afin de trouver l'indice de l'accent dans la liste.
    else: #Si la lettre n'est pas un accent, on l'ajoute directement au mot.
        mot_normalisé += lettre

