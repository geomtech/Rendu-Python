#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 25/02/2021
# Thème du script : Dictionnaire affiché en partant de la définition la plus longue.

def au_revoir():
    """
    affiche 3 sauts de ligne et Fin du programme
    Entrées : aucune
    Sortie : aucune
    """
    print("\n\n\nAu revoir\n\nFin du programme")

def sort_dict(dict_words: dict) -> list:
    """
    fait un tri le dictionnaire en paramètre
    Entrées :
        dict_words : dictionnaire de mots/définitions
    Sortie :
        retourne une liste qui contient pour tableau les mots associés à leurs définitions
    """
    sorted_words = []
    definitions_length = []

    for value in dict_words.values(): # Pour chaque définition du dico, on ajoute dans une liste la longueur de chaque définition 
        definitions_length.append(len(value))

    for value in dict_words.values(): # Pour chaque définition du dico
        if (len(value) in definitions_length): # On vérifie que la définition se trouve dans notre liste précédémment créée
            for word, definition in dict_words.items(): # Pour chaque mot/définition du dico
                if (len(definitions_length) > 0): # On vérifie que la liste de longueurs des définitions n'est pas vide afin d'éviter une erreur du à l'utilisation de la fonction max()
                    if (len(definition) == max(definitions_length)): # Si la longueur de la définition actuelle est la plus grande
                        sorted_words.append([word, definition]) # On ajoute le mot dans la liste car c'est le plus grand
                        definitions_length.remove(len(definition)) # Ensuite on supprime la longueur de la définition dans la liste afin que ce même mot ne soit plus traité.

    return sorted_words # On retourne la liste avec les mots/définitions triés

def display_dict(sorted_list: list) -> None:  
    """
    affiche la liste triée
    Entrées: 
        sorted_list : liste contenant des listes [mot, définition]
    Sortie :
        Aucune
    """  
    for definition in sorted_list: # Pour chaque définiton de la liste des associations mot/déf
        print(definition[0], "->", definition[1]) # On affiche sous le format "mot -> def"

################################################
########## PROGRAMME PRINCIPAL  ################
################################################

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
    
    sorted_dict = sort_dict(original_dict) # Appel de la fonction sort_dict avec le dico original et on associe la liste triée à sorted_dict
    display_dict(sorted_dict) # Appel de la fonction display_dict afin d'afficher le dico sous le bon format et trié

if __name__ == "__main__":
    main() # Appel de notre fonction principale
    au_revoir() # Appel de notre fonction pour quitter le programme
