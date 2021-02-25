#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 25/02/2021
# Thème du script : Dictionnaire affiché en partant de la définition la plus longue.

def sort_dict(dict_words: dict) -> list:
    sorted_words = []

    for key, value in dict_words.items():
        for definition in dict_words.values():
            print(len(value), len(definition))
            if (len(value) >= len(definition)):
                print(key)

    return sorted_words

def display_dict(sorted_list: list) -> None:
    pass
    #print(sorted_list)

def main() -> None:
    original_dict = {"Jeux": "On peut définir le jeu comme une activité de loisirs d'ordre physique ou bien psychique, soumise à des règles conventionnelles, à laquelle on s'adonne pour se divertir, tirer du plaisir et de l'amusement.",
            "Bouteille": "Récipient allongé à goulot étroit, en verre, en plastique, en métal ou en terre destiné aux liquides, notamment aux boissons",
            "Montre": "Une montre est un instrument de mesure du temps qui se porte sur soi.",
            "Pied": "Partie terminale du membre inférieur, articulée avec la jambe, permettant l'appui au sol dans la station debout et la marche.",
            "Table": "Meuble composé d'un plateau horizontal reposant sur un ou plusieurs pieds ou supports. Servant notamment pour les repas",
            "Chaise": "Siège à dossier, sans bras",
            "Chaise2": "Siège à dossier, sans pied",
            "Fauteuil": "Siège à dossier et à bras pour une personne",
            "Commode": "Meuble à hauteur d'appui garni, le plus souvent, de tiroirs",
            "Loup": "Animal feroce"}
    
    sorted_dict = sort_dict(original_dict)
    display_dict(sorted_dict)

if __name__ == "__main__":
    main()
