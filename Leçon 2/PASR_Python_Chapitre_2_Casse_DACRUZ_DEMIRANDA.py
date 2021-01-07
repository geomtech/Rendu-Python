#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 27/11/2020
# Thème du script : Changement de casse si c'est une lettre en input

# Init variable
lettre = ""

lettre = str(input("")) # On demande à l'utlisateur la lettre qu'il souhaite...

if "A" <= lettre <= "Z" : # Si lettre majuscule...
    print("Vous avez saisi la lettre majuscule ", str(lettre), ".\nAprès transformation en minuscule, on obtient la lettre ", str(lettre).lower() ,".", sep="")
elif "a" <= lettre <= "z": # Si lettre minuscule...
    print("Vous avez saisi la lettre minuscule ", str(lettre), ".\nAprès transformation en majuscule, on obtient la lettre ", str(lettre).upper() ,".", sep="")
else: # Si ce n'est pas une lettre...
    print("Vous avez saisi le caractère ", str(lettre), ", ce n'est pas une lettre.", sep="")
