#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 07/01/2021
# Thème du script : Multiplier son capital

def auRevoir():
    """
    affiche 3 sauts de ligne et Fin du programme
    Entrées : aucune
    Sortie : aucune
    """
    print("\n\n\nAu revoir\n\nFin du programme")

def CalculCapital(capital, taux, multiplicateur):
    nbreAnnees = 0
    capitalAttendu = capital * multiplicateur # Calcul du capital final attendu par l'utilisateur

    while (capital < capitalAttendu ) : # Augmentation du capital par le taux spécifié tant que le capital n'a pas dépassé l'attente de l'utilisateur
        capital = capital + (capital * taux)  # Calcul du capital final en y ajoutant le taux spécifié par l'utilisateur
        nbreAnnees += 1 # Comptage des années

    capital = round(capital, 2)  # Arrondir a deux décimal la variable capital
    return [nbreAnnees, capital]

capitalInitial = float(input("Quel est le capital initial ? ")) # Demande à l'utilisateur le capital initial
taux = float(input("Quel est le taux d'intérêt annuel (Pour 2%, on attend 0.02) ? ")) # Demande à l'utilisateur le taux d'interet
multiplicateur = float(input("Pour quel coefficient multiplicateur voulez vous avoir un prévision ? ")) # Demande à l'utilisateur le coefficient multiplicateur

capital = CalculCapital(capitalInitial, taux, multiplicateur) # Appelle fonction

taux = taux * 100 # Passage en %
capitalInitial = round(capitalInitial, 2) # arrondi à deux décimal

# Affichage du resultat
print( "Capital initial :" , capitalInitial,
        "\nTaux :" , taux, "%"
        "\nApres" , capital[0], "ans, votre capital aura été multiplié par" , multiplicateur)
print("Vous disposerez alors de :", capital[1])

auRevoir()  # On appelle la fonction pour quitter le programme
