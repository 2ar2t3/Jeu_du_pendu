import random
import string
alphabet = string.ascii_lowercase

def lecture_fichier():
    """Définition  d'une fonction qui lit le fichier
    de mots et le retourne sous forme de liste"""

    # Demande à l'utilisateur s'il possede une liste de mots.
    if input("Avez vous un fichier personnel .txt contenant une liste de mots "
             "pour jouer ? \n('oui' ou 'non') : ") == "non":
        #Ouverture, lecture et transformation de la chaines de texte en liste.
        return open('Liste_de_mots.txt', 'r', encoding='utf-8').read().split()

    #Vérification que le fichier donné par l'utilisateur existe bien
    while True:
        nom_fichier = input("Veuillez entrer le nom du fichier : ")
        try:
            with (open(f'{nom_fichier}.txt', 'r', encoding='utf-8') as liste_mots):
                return liste_mots.read().split()
        except FileNotFoundError:
            print("Le fichier est introuvable, veuillez reessayer.")


def choix_mot(liste):
    """Définition d'une fonction qui choisit un mot parmi
    la liste fournie et le retourne sans ses accents."""

    # Choix d'un mot au hasard dans la liste des mots.
    mot_a_trouver = random.choice(liste)

    # Création de deux chaines de charactères contenant les accents communs
    # possibles et leurs équivalents, en veillant à bien faire correspondre les indices.
    lettres_accentuees = "àâäéèêëîïôöùûüç"
    lettres_non_accentuees = "aaaeeeeiioouuuc"
    mot_normalise =""

    for lettre in mot_a_trouver:  #On itère sur chaque lettre du mot initial.

        # Si la lettre est un accent, on ajoute au mot, son équivalent sans accent
        if lettre in lettres_accentuees:
            # utilisation de find() afin de trouver l'indice de l'accent dans la liste.
            mot_normalise += lettres_non_accentuees[lettres_accentuees.find(lettre)]
        else:
            #Si la lettre n'est pas un accent, on l'ajoute directement au mot.
            mot_normalise += lettre
    return mot_normalise

def affichage_mot(lettres_testees, mot):
    """Fonction qui gère l'affichage du mot"""
    a_afficher = ""
    for i in range(len(mot)): #On itère sur chaque lettre du mot
        if mot[i] in lettres_testees: #Si la lettre à été devinée
            a_afficher += mot[i]
        else: #Si la lettre n'a pas été devinée
            a_afficher += "_"
    print(f"\n{a_afficher}")

    """ Cette partie permet de déterminer si le mot à été trouvé en entier 
    (servira pour la suite du code)."""
    # Si seulement des "_" sont affichés (toutes les lettres ont été trouvées.)
    if not "_" in a_afficher:
        return True
    return False

def jeu():
    """ Fonction principale du jeu. """
    jeu_en_cours = True

    print("Bienvenue dans le jeu du pendu !\nLes règles sont simples, "
          "vous allez devoir deviner un mot secret.."
          "\nLettre par lettre..\nMais attention, vous n'avez que 6 chances..\n")

    while jeu_en_cours:
        # Boucle principale du jeu, on sort lorsque le joueur ne souhaite plus jouer.

        mot_a_deviner = choix_mot(lecture_fichier())   #Initialisation du mot à deviner
        """ Définition de pluisieurs variables qui serviront par la suite. """
        vies = 6
        erreurs = 0
        tours = 0
        lettres_testees = []

        while erreurs < vies: #Boucle de la partie en cours.
            if tours == 0: #On écrit un message d'encouragement au premier tour.
                print("\nLa partie commence, bonne chance !")
                print(f'Le mot secret contient {len(mot_a_deviner)} lettres, '
                      f'essayez de les deviner, vous avez 6 essais.')
                affichage_mot(lettres_testees, mot_a_deviner)

            else: #à partir du tour 2
                print(f'\nIl vous reste {vies - erreurs} essais.')
                print(f'Lettres déjà essayées : {lettres_testees}')

            if (vies - erreurs) == 1 :
                while jeu_en_cours:
                    lettre_bonus = random.choice(string.ascii_lowercase)
                    if lettre_bonus not in mot_a_deviner:
                        break

                print(f"\nAttention, vous avez presques perdu..."
                      f"\nVoici un indice : la lettre '{lettre_bonus}' "
                      "n'est pas dans le mot secret.")

            while True:
                try:
                    lettre = input("\nVeuillez entrer une lettre à essayer : ")
                    if lettre not in alphabet :
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print(f"'{lettre}' n'est pas une lettre valide, "
                          "veuillez en entrer une.")
            lettres_testees.append(lettre)
            tours += 1

            # Affichage du mot et création d'une variable booléenne
            mot_trouve = affichage_mot(lettres_testees, mot_a_deviner)

            # L'utilisateur à trouvé une lettre dans le mot secret.
            if lettre in mot_a_deviner:

                # L'utilisateur à trouvé le mot entier
                if mot_trouve:
                    print(f'\nFélicitations, vous avez trouvé le mot secret !')
                    break #On sort de la boucle de la partie en cours.

                #L'utilisateur n'a pas encore trouvé le mot entier
                print(random.choice(["\nBien joué !", "\nBravo !", "\nJoli coup !"]))
                print(f'La lettre {lettre} est bel et bien dans le mot secret.')

            else: #L'utilisateur n'a pas trouvé de lettre dans le mot secret.
                print(random.choice(["\nAïe..",
                                     "\nC'est raté.",
                                     "\nCe n'est pas bon.."]))
                print(f"La lettre '{lettre}' n'est pas dans le mot secret.")
                erreurs += 1

        # L'utilisateur n'a pas trouvé le mot entier
        if not mot_trouve:
            print("\nLa partie est terminée, vous avez perdu..")
            print(f"Le mot à trouver était '{mot_a_deviner}'.")

        if input("\nSouhaitez-vous faire une nouvelle partie ? "
                 "('oui' / 'non') :\n") == 'non':
            # L'utilisateur ne veut plus jouer, on sort de la boucle principale du jeu.
            break

    print("\nTrès bien, merci d'avoir joué au jeu du pendu !")

jeu()