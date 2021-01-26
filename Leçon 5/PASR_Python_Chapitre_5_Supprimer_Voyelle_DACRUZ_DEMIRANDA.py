#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 26/01/2021
# Thème du script : Supprimer Voyelle

V = ""
L = []

def supprimerVoyelle(listeMot):
 
    for mot in listeMot:
        if (V in mot):
            listeMot.remove(mot)
        
    print(listeMot)



nbreValeurs= int(input("Combien de valeurs à ajouter dans la liste ?"))

for i in range(0, nbreValeurs):
    nouveauMot = str(input("Ajouter un mot:"))
    L.append(nouveauMot)
    
V = str(input("Supprimer les mots contenant la voyelle:"))


supprimerVoyelle(L)
