#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 27/11/2020
# Thème du script : Location de voitures

# Init variables constantes
location_tarif_essence = 40
kilometrage_tarif_essence = 0.15
location_tarif_diesel = 50
kilometrage_tarif_diesel = 0.10
jours = 0
kilometrage = 0

# Récupération des entrées par l'utilisateur
jours = int(input("Jours ? "))
kilometrage = int(input("Kilométrage ? "))

# Calcul des tarifs essence et diesel par rapport au nombre de kilometres et jours liés aux tarifs actuels de l'essence et du diesel
tarif_vehicule_essence = (kilometrage_tarif_essence * kilometrage) + (location_tarif_essence * jours)
tarif_vehicule_diesel = (kilometrage_tarif_diesel * kilometrage) + (location_tarif_diesel * jours)

# Affichage du résultat
print("Pour", jours, "jours et", kilometrage, "km")
print("avec un véhicule à essence:", tarif_vehicule_essence)
print("avec un véhicule diesel:", tarif_vehicule_diesel)

if tarif_vehicule_essence > tarif_vehicule_diesel: # Si le tarif essence est supérieur au diesel
    print("Véhicule diesel conseillé")
elif tarif_vehicule_diesel > tarif_vehicule_essence: # Si le tarif diesel est supérieur à l'essence
    print("Véhicule à essence conseillé")
else:
    print("Véhicule diesel et essence au même prix") # Si les deux sont égaux

# A quand les véhicules électriques ????
