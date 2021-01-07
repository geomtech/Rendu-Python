# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 1.0.0
# Date : 12/11/2020
# Explication : Donne à l'utilisateur une recette de crêpes adapté au nombre de personne(s).

# Importation du module math
import math

# Init variable
nb_personnes = 0

print("Pour la recette des crêpes, veuillez répondre à la question suivante :")

# Boucle pour demander à nouveau combien de personnes en cas d'erreur d'entré
while True:
    try:
        # On demande combien de personne
        nb_personnes = int(input("Pour combien de personnes ? "))

        # Déclenche une erreur si le nombre est négatif
        if (nb_personnes < 0):
            sys.exit()

        # Calcul des différentes doses multiplié par le nombre de personnes
        farine = math.ceil((250/8) * nb_personnes)
        oeufs = math.ceil((4/8) * nb_personnes)
        lait = math.ceil((50/8) * nb_personnes)
        beurre = math.ceil((50/8) * nb_personnes)
        sucre_vanille = math.ceil((10/8) * nb_personnes)
        rhum = math.ceil((5/8) * nb_personnes)

        # Affiche la recette des crêpes adaptée aux nombre de personnes
        print(f"""Pour {nb_personnes} personnes il faut :
        {farine} g de farine
        {oeufs} oeufs
        {lait} cl de lait
        1 pincée de sel
        {beurre} g de beurre
        {sucre_vanille} g de sucre vanillé
        {rhum} cl de rhum""")

    except:
        # Affiche message d'erreur en cas d'erreur déclenchée
        print("Erreur : Vous devez renseigner un entier positif.")
