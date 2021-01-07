#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 07/01/2021
# Thème du script : Losange vide : création d'un losange vide affiché à l'écran.

def auRevoir():
    """
    affiche 3 sauts de ligne et Fin du programme
    Entrées : aucune
    Sortie : aucune
    """
    print("\n\n\nAu revoir\n\nFin du programme")

def losangeVide(N, motif):
    """
    dessine un losange vide avec un certain motif pour les contours
    Entrées :
        N : la hauteur du losange (le nombre de lignes)
        motif : le caractère de dessin pour les contours
    Sortie :
        Affichage du losange vide
    Exemple :
        losangeVide(5, "*")
        dessine le losange ci-dessous
            *
           * *
          *   *
         *     *
        *       *
         *     *
          *   *
           * *
            *
    """ # on divise la hauteur par 2 pour avoir la hauteur d'un cote seulement (partie haute ou partie basse) soit deux triangles
    losange = [] # init tableau dans lequel se trouvera le losange

    for i in reversed(range(1, N)): # boucle partant de N à 1
        losange.append(' '*i + motif) # on ajoute le string généré au tableau losange

    losange.append(motif) # ligne du millieu

    for i in range(0, len(losange)): # boucle allant de 0 à la taille de la triangle haut du losange
        if (i > 0): # pour n'afficher que un motif pour la première et dernière ligne du losange
            spaces = (' '*(i))*2 # générer les espaces necessaires entre les motifs pour qu'il soit vide
            losange[i] = losange[i] + spaces[:-1] + motif # on modifie la ligne pour faire la partie droite du losange et ajouter entre les deux motifs le vide
        print(losange[i]) # on affiche la ligne

    # on genere le triangle bas pour compléter le losange
    for i in reversed(range(0, len(losange)-1)): # boucle partant de 0 à N
        print(losange[i]) # on affiche la ligne

################################################
########## PROGRAMME PRINCIPAL  ################
################################################


# L'utilisateur donne la hauteur
N = int(input("Quelle hauteur pour le losange ? "))
# L'utilisateur donne le motif pour les contours du losange
M = str(input("Quel motif pour le losange ? "))

if (N) >= 2:
    losangeVide(N, M)  # On appelle la fonction avec les différents paramètres

auRevoir()  # On appelle la fonction pour quitter le programme
