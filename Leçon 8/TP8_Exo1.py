#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 01/04/2021
# Thème du script : Exo 1

import argparse
import re

def au_revoir():
    """
    affiche 3 sauts de ligne et Fin du programme
    Entrées : aucune
    Sortie : aucune
    """
    print("\n\n\nAu revoir\n\nFin du programme")

def parse_file(filename: str):
    # Ouvre le fichier
    with open(filename, "r") as file_to_parse:
        for line in file_to_parse:
            parse(line)

def parse(line):
    print(line)

def main():
    # Parsing des arguments lancé dans le CLI
    parser = argparse.ArgumentParser()

    # Argument pour le nom du fichier à parser
    parser.add_argument("filename", help="Nom du fichier à parser.", type=str)

    args = parser.parse_args()

    # Assignation de la valeur de l'argument filename
    filename = args.filename

    parse_file(filename)

if __name__ == "__main__":
    main()  # Appel de notre fonction principale
    au_revoir()  # Appel de notre fonction pour quitter le programme
