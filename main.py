import random


def Lecture_fichier():
    """Définition  d'une fonction qui lit le fichier de mots et le retourne sous forme de liste"""
    if input("Avez vous un fichier personnel .txt contenant une liste de mots pour jouer ? ('oui' ou 'non') : ") == "oui": # Demande à l'utilisateur si il poss_de une liste de mots.
        Nom_fichier = input("Veuillez entrer son nom (sans l'extention): ")
    else:
        Nom_fichier = "Liste_de_mots" #Utilisation de la liste originale.

    # Ouverture du fichier, lecture et transformation de la chaine de charactères en une liste de mots.
    Liste_mots = open(f'{Nom_fichier}.txt', 'r', encoding='utf-8').read().split()
    return Liste_mots


def Choix_mot(Liste):
    """Définitiojn d'une fonction qui choisit un mot parmi la liste fournie et le retourne sans ses accents."""
    Mot_a_trouver = Liste[random.randint(0, len(Liste) - 1)] #Choix d'un mot au hasard dans la liste des mots.

    lettres_accentuées = "àâäéèêëîïôöùûüç" #Création de deux chaines de charactères contenant les accents possibles et leurs équivalents en veillant à bien faire correspondre les indices.
    lettres_non_accentuées = "aaaeeeeiioouuuc"
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

    if not "_" in a_afficher: #Cette partie permet de déterminer si le mot à été trouvé (servira pour la suite du code).
        return True
    return False

def jeu():
    """ Fonction principale du jeu. """

    jeu_en_cours = True

    while jeu_en_cours: #Boucle principale du jeu, on sort lorsque le joueur ne souhaite plus jouer.

        mot_a_deviner = Choix_mot(Lecture_fichier())  # Création d'une variable locale dans la fonction.
        # Définition de pluisieurs variables qui serviront par la suite.
        Vies = 6
        Erreurs = 0
        Tours = 0
        Lettres_testées = []

        while Erreurs < Vies: #Boucle de la partie en cours.
            if Tours == 0: #On écrit un message d'encouragement au premier tour.
                print("La partie commence, bonne chance !")
                print(f'Le mot secret contient {len(mot_a_deviner)} lettres, essayez de les deviner, vous avez 6 essais.')
            else:
                print(f'\nIl vous reste {Vies - Erreurs} essais.')
                print(f'Lettres déjà essayées : {Lettres_testées}')

            mot_trouvé = Affichage_mot(Lettres_testées, mot_a_deviner)#Affichage du mot

            Lettre = input("Veuillez entrer une lettre à essayer : ")
            Lettres_testées.append(Lettre)
            Tours += 1

            if Lettre in mot_a_deviner: #L'utilisateur à trouvé une lettre dans le mot secret.
                if mot_trouvé: #L'utilisateur à trouvé le mot entier.
                    print(f'\nFélicitations, vous avez trouvé le mot secret qui était : {mot_a_deviner} !')
                    break
                print(random.choice(["\nBien joué !", "\nBravo !", "\nJoli coup !"]))
                print(f'La lettre {Lettre} est bel et bien dans le mot secret.')

            else: #L'utilisateur n'a pas trouvé de lettre dans le mot secret.
                print(random.choice(["\nAïe..", "\nC'est raté.", "\nCe n'est pas bon.."]))
                print(f"La lettre '{Lettre}' n'est pas dans le mot secret.")
                Erreurs += 1

        if not Affichage_mot(Lettres_testées, mot_a_deviner):
            print("\nLa partie est terminée, vous avez perdu..")
            print(f"Le mot à trouver était '{mot_a_deviner}'.")

        if input("\nSouhaitez-vous faire une nouvelle partie ? ('oui' / 'non') :\n") == 'non':
            break
    print("\nTrès bien, merci d'avoir joué au jeu du pendu !")

jeu()