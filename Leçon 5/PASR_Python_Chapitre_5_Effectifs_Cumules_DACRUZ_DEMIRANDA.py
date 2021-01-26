#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 26/01/2021
# Thème du script : Effectifs cumulés d'une liste :
#                   Ecrire un programme qui attend une liste L d'entiers et qui affiche les effectifs cumulés des 
#                   différents éléments de la liste sous forme de bâtons constitués d'étoiles.

def auRevoir():
    """
    affiche 3 sauts de ligne et Fin du programme
    Entrées : aucune
    Sortie : aucune
    """
    print("\n\n\nAu revoir\n\nFin du programme")

def AfficherEffectifs(liste): 
    """
    affiche les effectifs cumulés des différents éléments de la 
    liste sous forme de bâtons constitués d'étoiles.
    Entrées :
        liste : Liste [] contenant les valeurs qui seront traitées pour calculer les
                effectifs cumulés dans cette même liste.
    Sortie : aucune
    """
    effectifs = [] # création de la liste des effectifs

    for value in liste: # pour chaque valeur de la liste L
        stars_count = 0 # compteur d'effectif

        for number in liste: # pour chaque nombre de la liste L
            if (value == number): # ça permet de compter le nombre d'effectifs de la liste
                stars_count += 1 # on ajoute +1 étoile
        
        effectif_item = [stars_count, value] # on créé une liste contenant le nombre d'étoiles ainsi que la valeur associée

        if effectif_item not in effectifs: # si on ne l'a pas déjà dans la liste
            effectifs.append([stars_count, value]) # on ajoute ce compteur d'effectifs
    
    for effectif in effectifs: # Pour chaque effectif
        stars_str = "*"*int(effectif[0]) # On compte les étoiles
        print(stars_str, effectif[1]) # et on affiche les étoiles avec la valeur associée

################################################
########## PROGRAMME PRINCIPAL  ################
################################################

L = [] # création de la liste L
nb_values = int(input("Nombre de valeurs à ajouter dans la liste ? ")) # On demande le nombre de valeurs de la liste

for i in range(0, nb_values): # On demande la valeur a ajouter par rapport au nombre de valeurs entrée précédemment
    value = int(input("Valeur à ajouter : ")) 
    L.append(value) # On ajoute la valeur entrée

AfficherEffectifs(L) # on affiche les cumuls d'effectifs
auRevoir() # on quitte le programme
