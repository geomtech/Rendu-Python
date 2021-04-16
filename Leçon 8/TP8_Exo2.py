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
    capital_numbers = []
    dots = []
    three_dots = []
    hexadecimal = []
    chars_12_alphanumeric = []
    contains_5_letters_a = []

    output.append("""*************************************************
PYTHON : Fichier de sortie de l'exercice 2 du TP4
*************************************************
    """)

    # Ouvre le fichier
    with open(filename, "r") as file_to_parse:
        for line in file_to_parse:
            line = line.replace('\n', '')
            if parse_capital_numbers(line):
                capital_numbers.append(line)
            if parse_dots(line):
                dots.append(line)
            if parse_three_dots(line):
                three_dots.append(line)
            if parse_hexadecimal(line):
                hexadecimal.append(line)
            if parse_12_chars_alphanumeric(line):
                chars_12_alphanumeric.append(line)
            if parse_contains_5_letters_a(line):
                contains_5_letters_a.append(line)


    output.append("""*****************************************************
1.a : lignes contenant des chiffres ou des majuscules
*****************************************************""")

    count_1a = "***** " + str(len(capital_numbers)) + " lignes trouvees *****\n"
    for line in capital_numbers:
        output.append(line)
    output.append(count_1a)

    output.append("""*********************************
1.b : lignes contenant des points
*********************************""")

    count_1b = "***** " + str(len(dots)) + " lignes trouvees *****\n"
    for line in dots:
        output.append(line)
    output.append(count_1b)

    output.append("""***********************************
1.c : lignes contenant trois points
***********************************""")

    count_1c = "***** " + str(len(three_dots)) + " lignes trouvees *****\n"
    for line in three_dots:
        output.append(line)
    output.append(count_1c)

    output.append("""**********************************************************************
1.d : lignes contenant des nombres hexadecimaux separes par des blancs
**********************************************************************""")

    #count_1d = "***** " + str(len(hexadecimal)) + " lignes trouvees *****\n"
    #for line in hexadecimal:
    #    output.append(line)
    #output.append(count_1d)

    output.append("""**********************************************************************
1.e : lignes contenant un mot d'au moins 12 caracteres alphanumeriques
**********************************************************************""")

    count_1e = "***** " + str(len(chars_12_alphanumeric)) + " lignes trouvees *****\n"
    for line in chars_12_alphanumeric:
        output.append(line)
    output.append(count_1e)

    output.append("""*******************************************************************************
1.f : lignes contenant exactement 5 lettres a (pas nécessairement successives)
*******************************************************************************""")

    count_1f = "***** " + str(len(contains_5_letters_a)) + " lignes trouvees *****\n"
    for line in contains_5_letters_a:
        output.append(line)
    output.append(count_1f)

    return output

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
    if re.search(r'\.\.\.', line):
        return True
    return False


# Contient un hexadécimal isolé
# TODO
def parse_hexadecimal(line):
    if re.search(r'\A[0-9A-F]+\Z', line):
        return True
    return False


# Contient un mot d'au moins 12 caractères alphanumériques
def parse_12_chars_alphanumeric(line):
    if re.search(r'[0-z]{12}', line):
        return True
    return False


# Contient un mot d'au moins 12 caractères alphanumériques
def parse_contains_5_letters_a(line):
    if re.search(r'([^a]*a){5,5}', line):
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

    for line in parse_file(filename, output):
        print(line)


if __name__ == "__main__":
    main()  # Appel de notre fonction principale
    au_revoir()  # Appel de notre fonction pour quitter le programme
