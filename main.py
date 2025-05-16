import random


def Lecture_fichier():
    """Définition  d'une fonction qui lit le fichier de mots et le retourne sous forme de liste"""
    if input("Avez vous un fichier contenant une liste de mots pour jouer ? ('oui' ou 'non') : ") == "oui": # Demande à l'utilisateur si il poss_de une liste de mots.
        Nom_fichier = input("Veuillez entrer le nom du fichier contenant la liste des mots (avec l'extension): ")
    else:
        Nom_fichier = "Liste_de_mots.txt" #Utilisation de la liste originale.
    Liste_mots = open(f'{Nom_fichier}', 'r', encoding='utf-8').read().split() #Ouverture du fichier, lecture et transformation de la chaine de charactères en une liste de mots.
    return Liste_mots


def Choix_mot(Liste):
    """Définitiojn d'une fonction qui choisit un mot parmi la liste fournie et le retourne sans ses accents."""
    Mot_a_trouver = Liste[random.randint(0, len(Liste) - 1)] #Choix d'un mot au hasard dans la liste des mots.

    lettres_accentuées = "àâäéèêëîïôöùûüçÀÂÄÉÈÊËÎÏÔÖÙÛÜÇ" #Création de deux chaines de charactères contenant les accents possibles et leurs équivalents en veillant à bien faire correspondre les indices.
    lettres_non_accentuées = "aaaeeeeiioouuucAAAEEEEIIOOUUUC"
    mot_normalisé =""

    for lettre in Mot_a_trouver:  #On itère sur chaque lettre du mot initial.
        if lettre in lettres_accentuées: #Si la lettre est un accent, on ajoute au mot, son équivalent sans accent
            mot_normalisé += lettres_non_accentuées[lettres_accentuées.find(lettre)] #utilisation de find() afin de trouver l'indice de l'accent dans la liste.
        else:
            mot_normalisé += lettre #Si la lettre n'est pas un accent, on l'ajoute directement au mot.
    return mot_normalisé

def Affichage_mot(lettres_testees, mot):
    """Fonction qui gère l'affichage du mot"""
    a_afficher = ""
    for i in range(len(mot)):
        if mot[i] in lettres_testees:
            a_afficher += mot[i]
        else:
            a_afficher += "_"
    print(a_afficher)

def jeu():
    """ Fonction principale du jeu. """
    mot_a_deviner = Choix_mot(Lecture_fichier()) #Création d'une variable locale dans la fonction.
    Vies = 6
    Erreurs = 0
    Bonnes_reponses = 0
    Lettres_testées = []
    Victore = False

    test = 0

    while Erreurs < Vies or Victore:
        Affichage_mot(Lettres_testées, mot_a_deviner)
        Lettre = input("Veuillez entrer une lettre : ")
        Lettres_testées.append(Lettre)

        if Lettre in mot_a_deviner:
            Bonnes_reponses += 1
            if Bonnes_reponses == len(mot_a_deviner):
                print(f'Félicitations, tu as trouvé le mot secret qui était : {mot_a_deviner} !')
                Victore = True
                break
            random.choice((print("Bien joué"),print("Bravo"),print("Joli coup")))
            print(f'La lettre {Lettre} est bel et bien dans le mot secret !')
        else:
            random.choice((print("Aïe"),print("Raté"),print("C'est pas bon")))
            print(f'La lettre {Lettre} n\'est pas dans le mot secret !')
            Erreurs += 1



jeu()