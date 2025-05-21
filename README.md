# Jeu du pendu 

Ce dépot contient le jeu du pendu codé en Python. 
L'objectif dans ce jeu est de deviner, lettre par lettre, un mot secret avec un nombre limité d'essais. 

## Le dépot contient
- Un fichier main.py contenant le jeu.
- Un fichier Liste_de_mots.txt contenant une liste de mots par défaut.

## Utilisation du jeu 
Aucun requis d'installation autre que python 3 n'est nécessaire pour l'utilisation du jeu. Il suffit de lancer le script main.py dans un terminal python.  
Il suffit de répondre aux questions posées dans le terminal pour jouer. 
Les seules entrées possibles de l'utilisateurs sont : 
- "oui"/"non"
- "a", "b", "c", ..., "y", "z"
- f"{nom_du_fichier_personnel}"

Une entrées différente de celles listés ci-dessus donnera inévitablement une erreur et l'utilisateur sera demandé de réitérer son entrée.

Pour fournir sa propre liste de mot il suffit de répondre "oui" à la question 
"Avez vous un fichier personnel .txt contenant une liste de mots pour jouer ? \n('oui' ou 'non') : ", puis d'indiquer le nom du fichier sans l'extention. 

## Le code respecte les exigences de base suivantes 
- Le mot secret est sélectionné aléatoirement parmi une liste de mots.
- Un état actuel du mot est affiché à chaque tour avec les lettres devinées et non devinées (remplacées par des '_').
- L'utilisateur choisi la lettre qu'il souhaite tester.
- Le code indique à l'utilisateur si la lettre faisait partie du mot ou non.
- Le nombre d'essai de l'utilisateur est mis à jour à chaque tour jusqu'à victoire ou défaite.

### Mais aussi des exigences additionnelles 
- L'utilisateur peut fournir un fichier personnel .txt contenant sa propre liste de mot, sinon le fichier par défaut est utilisé.
- Les mots contenant des accents sont normalisés sans accents afin de facilité le jeu.
- Le programme propose à l'utilisateur de rejouer s'il le souhaite à la fin d'une partie.
- Lorsque l'utilisateur n'a plus qu'un seul éssai, un indice lui est donné (une lettre ne faisant pas parti du mot secret).
- Les entrées de l'utilisateur (lettre à tester, fichier à utiliser) sont vérifiées par le code pour attester de leur validité (la lettre est bien une lettre
  de l'alphabet, le fichier de mot personnel existe bien).



