# on a pour départ, un chiffre aléatoire qui est choisi
# aprés, le jeu nous demande de taper un nombre entre 0 et 100
# si la réponse est inférieur au nombre aléatoire 
# il doit afficher "le nombre le plus grand"
# si la réponse est supérieur au nombre aléatoire
# il doit afficher "le nombre est plus petit"
# et sinon, vous avez gagné

# ici, on importe une librairie qui contient
# des fonctions aléatoires
import random

# initialise nos variables nbAléatoire et trouver
# nb aléatoire sera générer par l'ordinateur 
# trouver est un boolean qui est égale à Faux
nbAléatoire = random.randrange(0,100)
trouver = False

# Tant que trouver est égale à Faux, on continue
while trouver == False:
    print("tape un nombre entre 0 et 100")
    # on convertit le nombre tape au clavier en int 
    réponse = int( input() )

    # on compare notre réponse avec le nb aléatoire
    if réponse < nbAléatoire:
        print ("le nombre est plus grand")
    elif réponse > nbAléatoire :
        print ("le nombre est plus petit")
    else :
        print ("vous avez gagné !")
        # on passe trouver à vrai pour arrêter la boucle
        trouver = True