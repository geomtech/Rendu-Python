#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 11/12/2020
# Thème du script : Rectangle vide : création d'un rectangle vide affiché à l'écran.

def auRevoir():
    """
    affiche 3 sauts de ligne et Fin du programme
    Entrées : aucune
    Sortie : aucune
    """
    print("\n\n\nAu revoir\n\nFin du programme")

def rectangleVide(hauteur, largeur, motif):
    """
    dessine un rectangle vide avec un certain motif pour les contours
    Entrées :
        hauteur : la hauteur du rectangle (le nombre de lignes)
        largeur : la largeur du rectangle (nombre de colonnes)
        motif : le caractère de dessin pour les contours
    Sortie :
        Affichage du rectangle vide
    Exemple :
        rectangleVide(6 , 5 , "*")
        dessine le rectangle ci-dessous
        *****
        *   *
        *   *
        *   *
        *   *
        *****
    """
    for i in range(0, hauteur): # Boucle for allant de ligne à ligne par rapport à la hauteur rentré
        if (i == 0) or (i == hauteur-1): # Si première et dernière ligne
            print(largeur*motif) # On affiche une ligne pleine
        else:
            print(motif + (" " * (largeur-2)) + motif) # On affiche une ligne avec le motif pour premier et dernier caractère avec des espaces entre deux

################################################
########## PROGRAMME PRINCIPAL  ################
################################################

H = int(input("Quelle hauteur pour le rectangle ? ")) # L'utilisateur donne la hauteur
L = int(input("Quelle largeur pour le rectangle ? ")) # L'utilisateur donne la largeur
M = str(input("Quel motif pour le rectangle ? ")) # L'utilisateur donne le motif pour les contours du triangle

rectangleVide(H , L , M) # On appelle la fonction avec les différents paramètres

auRevoir() # On appelle la fonction pour quitter le programme
