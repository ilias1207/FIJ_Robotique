#il existe 3 types de variables sous python

variable1 = 5 # integer > int qui symbolise un nombre entier
variable2 = 3.2 # float > float qui symbolise un chiffre à virgule
variable3 = "Coucou" # string > str qui symbolise du texte

#Fonction qui permet d'afficher du texte 
# à l'écran
print("du texte", variable1, variable2, variable3)

#Fonction permettant de connaitre le type d'une variable
print( type(variable1) )

typeDeVariable = type(variable1)

print("le type de la variable1 =", typeDevariable)

#Ici, on modifie le type de variable
variable1 = str(variable1)

typeDeVariable = type(variable1)
print("le type de la variable1 =", typeDevariable)

#En python, il existe plusieurs opérateurs
# addition          > +
# soustraction      > -
# multiplication    > *
# l'exposant        > **
# division          > /
# division entière  > //
# modulo            > %

