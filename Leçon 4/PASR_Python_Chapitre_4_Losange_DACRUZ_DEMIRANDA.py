#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 07/01/2021
# Thème du script : Rectangle vide : création d'un losange vide affiché à l'écran.

def auRevoir():
    """
    affiche 3 sauts de ligne et Fin du programme
    Entrées : aucune
    Sortie : aucune
    """
    print("\n\n\nAu revoir\n\nFin du programme")

def losangeVide(N, motif):
    """
    dessine un rectangle vide avec un certain motif pour les contours
    Entrées :
        hauteur : la hauteur du rectangle (le nombre de lignes)
        motif : le caractère de dessin pour les contours
    Sortie :
        Affichage du rectangle vide
    Exemple :
        rectangleVide(5, "*")
        dessine le rectangle ci-dessous
            *
           * *
          *   *
         *     *
        *       *
         *     *
          *   *
           * *
            *
    """
    N_Triangle = int(N/2)
    triangle_up = []
    triangle_down = []

    for i in reversed(range(1, N_Triangle)):  
        triangle_up.append(' '*i + motif)
    for i in range(0, len(triangle_up)):  
        if (i > 0):
            spaces = (' '*(i))*2
            triangle_up[i] = triangle_up[i] + spaces[:-1] + motif
        print(f"#{i}", triangle_up[i])

    print("#i", motif, " "*N_Triangle, motif)

    for i in range(1, N_Triangle):
        triangle_down.append(' '*i + motif)
    for i in reversed(range(0, len(triangle_down))):
        print(f"#{i}", triangle_down[i])

################################################
########## PROGRAMME PRINCIPAL  ################
################################################


# L'utilisateur donne la hauteur
N = int(input("Quelle hauteur pour le rectangle ? "))
# L'utilisateur donne le motif pour les contours du losange
M = str(input("Quel motif pour le losange ? "))

if (N) >= 2:
    losangeVide(N, M)  # On appelle la fonction avec les différents paramètres

auRevoir()  # On appelle la fonction pour quitter le programme
