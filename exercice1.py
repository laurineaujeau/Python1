nom=input('Entrez votre nom >')
nbEssai = 1
import random
valAlea=random.randint(0,20)
while nbEssai<7:
    print('Essai '+str(nbEssai)+'/6') # toujours forcer le type d'une variable à afficher
    val=input('Entrez un nombre entre 0 et 20 >')
    if not val.isdigit() :
        print('Entier incorrect')
    elif int(val)<0 or int(val)>20 :# toujours forcer le type d'une variable à comparer
        print('Entier incorrect')
    elif valAlea<int(val):
        print('Le nombre est plus petit')
        nbEssai=nbEssai+1
    elif valAlea>int(val):
        print('Le nombre est plus grand')
        nbEssai=nbEssai+1
    elif valAlea==int(val):
        print('Bravo ! Vous avez gagné '+nom)
        break
