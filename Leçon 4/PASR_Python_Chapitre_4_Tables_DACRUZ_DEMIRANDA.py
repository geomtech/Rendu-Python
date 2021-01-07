#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 07/01/2021
# Thème du script : Tables de multiplication à répétition

def auRevoir():
    """
    affiche 3 sauts de ligne et Fin du programme
    Entrées : aucune
    Sortie : aucune
    """
    print("\n\n\nAu revoir\n\nFin du programme")

def AfficherTableMultiplication(entier): 
    """
    affiche la table de multiplication et un saut de ligne
    Entrées : 
        entier : entier dont on souhaite connaitre la table de multiplications
    Sortie :
        Affichage de la table de multiplication
    """
    for multiplier in range(1,11): # de 1, 2, 3...9 à 10
        result = entier*multiplier  # on calcule l'entier multiplie par 1, 2, 3...9 à 10
        print(entier, "x", multiplier, "=", result) # on affiche chaque ligne de la table de multiplication avec les valeurs correspondantes
    print() # on saute une ligne

################################################
########## PROGRAMME PRINCIPAL  ################
################################################

entier_positif = True

while (entier_positif): # Tant que l'entier en input est positif
    input_entier = int(input("Entier > ")) # L'utilisateur donne l'entier pour connaître la table de multiplication lui correspondant

    if (input_entier <= -1): # si la valeur entre par l'utilisateur est negative
        entier_positif = False # on met la variable sur false et donc on arrête la boucle while
        auRevoir() # on quitte le programme
    else: # sinon
        AfficherTableMultiplication(input_entier) # on affiche la table de multiplication
