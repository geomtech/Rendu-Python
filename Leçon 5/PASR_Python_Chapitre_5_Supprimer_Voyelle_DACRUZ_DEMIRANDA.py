#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 26/01/2021
# Thème du script : Supprimer Voyelle

def auRevoir():
    """
    affiche 3 sauts de ligne et Fin du programme
    Entrées : aucune
    Sortie : aucune
    """
    print("\n\n\nAu revoir\n\nFin du programme")

def supprimerVoyelle(listeMot, voyelle):
    """
    affiche une liste de mot dans laquelle on a retirer 
    les mots contenant une voyelle sélectionnée
    Entrée : 
        listeMot : liste de mots
        voyelle  : voyelle à trouver dans les mots
    Sortie : affiche la liste de mot sans la voyelle sélectionnée
    """
    for mot in listeMot: # Pour chaque mot de la liste:
        if (V in mot): # Si l'on trouve la voyelle sélectionnée:
            listeMot.remove(mot) # Suppression du mot contenant la voyelle sélectionnée.
        
    print(listeMot) # Affichage de la liste modifiée

################################################
########## PROGRAMME PRINCIPAL  ################
################################################

# Initialisation des variables
V = ""
L = []

nbreValeurs= int(input("Combien de valeurs à ajouter dans la liste ?")) # Demande à l'utilisateur d'entrer la longueur de la liste

for i in range(0, nbreValeurs): # Boucle for permettant à l'utilisateur de renseigner autant de mot que la longueur de la liste
    nouveauMot = str(input("Ajouter un mot:")) 
    L.append(nouveauMot)  # ajout du nouveau mot à la liste

V = str(input("Supprimer les mots contenant la voyelle:")) # Demande à l'utilisateur de choisir la voyelle pour supprimer les mots contenant celle-ci

supprimerVoyelle(L, V)  # Appelle la fonction "supprimerVoyelle" avec la liste L
auRevoir() # on quitte le programme
