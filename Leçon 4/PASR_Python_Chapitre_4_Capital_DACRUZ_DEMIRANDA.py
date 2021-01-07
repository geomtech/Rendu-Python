#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 07/01/2021
# Thème du script : Multiplier son capital


# Initialisation des variables
capitalInitial = 0
taux = 0
multiplicateur = 0
capitalFinalAttendu = 0
capitalFinal = 0
nbreAnnees = 0

capitalInitial = float(input("Quel est le capital initial ? "))  # Demande à l'utilisateur le capital initial
taux = float(input("Quel est le taux d'intérêt annuel (Pour 2%, on attend 0.02) ? ")) # Demande à l'utilisateur le taux d'interet
multiplicateur = float(input("Pour quel coefficient multiplicateur voulez vous avoir un prévision ? ")) # Demande à l'utilisateur le coefficient multiplicateur 

capitalFinalAttendu = capitalInitial * multiplicateur # Calcul du capital final attendu par l'utilisateur
capitalFinal = capitalInitial  # Mise à jour de la variable capitalFinal

while (capitalFinal < capitalFinalAttendu ) : # Augmentation du capital par le taux spécifié tant que le capital n'a pas dépassé l'attente de l'utilisateur
    capitalFinal = (capitalFinal + (capitalFinal * taux))  # Calcul du capital final en y ajoutant le taux spécifié par l'utilisateur
    nbreAnnees += 1 # Comptage des années

taux = taux*100 # Passage du taux en pourcentage
capitalInitial = round (capitalInitial) # Arrondir a deux décimal la variable capitalInitial
capitalFinal = round (capitalFinal) # Arrondir a deux décimal la variable capitalFinal

# Affichage du resultat
print ( "Capital initial :" ,capitalInitial, 
        "\n Taux :" ,taux, "%"
        "\n Apres" ,nbreAnnees, "ans, votre capital aura été multiplié par" ,multiplicateur,
        "\n Vous disposerez alors de :" ,capitalFinal
        )
