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

def AfficherTableMultiplication(n, p, entier): 
    """
    affiche la table de multiplication et un saut de ligne
    Entrées : 
        n : Valeur de depart
        p : Valeur d'arrivee
        entier : entier dont on souhaite connaitre la table de multiplications
    Sortie :
        Affichage de la table de multiplication
    """
    for multiplier in range(n,p+1): # de n à p
        result = entier*multiplier  # on calcule l'entier multiplie
        print(entier, "x", multiplier, "=", result) # on affiche chaque ligne de la table de multiplication avec les valeurs correspondantes
    print() # on saute une ligne

################################################
########## PROGRAMME PRINCIPAL  ################
################################################

entier_positif = True

while (entier_positif): # Tant que l'entier en input est positif
    e = int(input("Table de ? ")) # L'utilisateur donne l'entier pour connaître la table de multiplication lui correspondant
    n = int(input(f"Quelle valeur de départ pour la table de {e} ? "))
    p = int(input(f"Quelle valeur d'arrivée pour la table de {e} ? "))

    if (e <= -1): # si la valeur entre par l'utilisateur est negative
        entier_positif = False # on met la variable sur false et donc on arrête la boucle while
        auRevoir() # on quitte le programme
    else: # sinon
        AfficherTableMultiplication(n, p, e) # on affiche la table de multiplication
