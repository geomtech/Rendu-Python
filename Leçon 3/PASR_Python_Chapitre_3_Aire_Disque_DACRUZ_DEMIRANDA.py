#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 11/12/2020
# Thème du script : Aire Disque

from math import pi as Pi # on importe pi du module math et on l'appelle Pi

def auRevoir():
    """
    affiche 2 sauts de ligne et Fin du programme
    Entrées : aucune
    Sortie : aucune
    """
    print("\n\nAu revoir\n\nFin du programme")

def aireDisque(rayon): 
    '''
    Cette fonction affiche 2 sauts de ligne, calcul et affiche l'aire d'un disque en fonction de son rayon
    Entrées : 
        rayon : cette valeur correspond au rayon du disque en cm
    Sortie :
        aire : affichage de l'aire calculée en fonction du rayon
        erreur : affiche un message d'erreur
    Exemple : 
        aireDisque(19.8)
        retourne le résultat suivant :
        L'aire d'un disque de rayon 19.8 est 1231.6299839133426
    '''
    if (rayon > 0) : # Si le rayon est supérieur à 0
        aire = Pi * rayon ** 2 # Calcul de l'aire du disque
        print("\n\nUn disque avec un rayon de" ,rayon, "cm, a une aire de" ,aire, "cm².")  # Affiche le résultat
    else : # Si le rayon est inférieur à 0
        print("\n\nVeuillez entrer une valeur positive")


################################################
########## PROGRAMME PRINCIPAL  ################
################################################

rayon = float(input("\n\nQuel est le rayon du disque en cm ? ")) # Demande à l'utilisateur le rayon du disque en cm

aireDisque(rayon) # Appel de la fonction aireDisque avec le paramètre "rayon" défini précédemment

auRevoir() # On appelle la fonction pour quitter le programme