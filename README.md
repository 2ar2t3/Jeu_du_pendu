# Jeu du pendu 

Ce dépot contient le jeu du pendu codé en Python. 
L'objectif dans ce jeu est de deviner, lettre par lettre, un mot secret avec un nombre limité d'essais. 

## Le dépot contient
- Un fichier main.py contenant le jeu.
- Un fichier Liste_de_mots.txt contenant une liste de mots par défaut.

## Utilisation du jeu 
Aucun requis d'installation autre que python 3 n'est nécessaire pour l'utilisation du jeu. Il suffit de lancer le script main.py dans un terminal python.  

## Le code respecte les exigences de base suivantes 
- Le mot secret est sélectionné aléatoirement parmi une liste de mots.
- Un état actuel du mot est affiché à chaque tour avec les lettres devinées et non devinées (remplacées par des '_').
- L'utilisateur choisi la lettre qu'il souhaite tester.
- Le code indique à l'utilisateur si la lettre faisait partie du mot.
- Le nombre d'essai de l'utilisateur est mis à jour à chaque tour jusqu'à victoire ou défaite.

### Mais aussi des exigences additionnelles 
- L'utilisateur peut fournir un fichier personnel .txt contenant sa liste de mot, sinon le fichier par défaut est utilisé.
- Les mots contenant des accents sont normalisés sans accents afin de facilité le jeu.
- Le programme propose à l'utilisateur de rejouer s'il le souhaite à la fin d'une partie.
- Lorsque l'utilisateur n'a plus qu'un seul éssai, un indice lui est donné.
- Les entrées de l'utilisateur (lettre à tester, fichier à utiliser) sont vérifiées par le code pour attester de leur validité.

Pour fournir sa propre liste de mot il suffit de répondre "oui" à la question 
"Avez vous un fichier personnel .txt contenant une liste de mots pour jouer ? \n('oui' ou 'non') : ", puis d'indiquer le nom du fichier sans l'extention. 

## Exemple d'utilisation : 
A FAIRE 
