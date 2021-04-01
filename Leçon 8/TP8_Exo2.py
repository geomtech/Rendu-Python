#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 01/04/2021
# Thème du script : Exo 2

import argparse
import re


def au_revoir():
    """
    affiche 3 sauts de ligne et Fin du programme
    Entrées : aucune
    Sortie : aucune
    """
    print("\n\n\nAu revoir\n\nFin du programme")


def parse_file(filename: str, output_filename: str):
    output = []

    # Ouvre le fichier
    with open(filename, "r") as file_to_parse:
        for line in file_to_parse:
            parse_line(line, output)

# Méthodes de parsing
def parse_line(line, output):
    if parse_capital_numbers(line):
        output.append(line)
    if parse_dots(line):
        output.append(line)
    if parse_three_dots(line):
        output.append(line)
    if parse_hexadecimal(line):
        output.append(line)

# Contient une majuscule ou un chiffre
def parse_capital_numbers(line):
    if re.search('[A-Z0-9]', line):
        return True
    return False


# Contient un point
def parse_dots(line):
    if re.search(r'\.', line):
        return True
    return False


# Contient trois points
def parse_three_dots(line):
    if re.search(r'\...', line):
        return True
    return False


# Contient un hexadécimal isolé
# TODO
def parse_hexadecimal(line):
    if re.search(r'\s[A-F][0-9]\s', line):
        return True
    return False


def main():
    # Parsing des arguments lancé dans le CLI
    parser = argparse.ArgumentParser()

    # Argument pour le nom du fichier à parser
    parser.add_argument("filename", help="Nom du fichier à parser.", type=str)
    parser.add_argument("output", help="Nom du fichier de sortie pour les résultats de parsing.", type=str)

    args = parser.parse_args()

    # Assignation de la valeur de l'argument filename
    filename = args.filename
    output = args.output

    parse_file(filename, output)


if __name__ == "__main__":
    main()  # Appel de notre fonction principale
    au_revoir()  # Appel de notre fonction pour quitter le programme
