#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.2
# Date : 28/04/2021
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


def afficheTitre(titre: str):
    longueurTitre = len(titre)
    etoiles = "*"*longueurTitre
    renduTitre = etoiles + "\n" + titre + "\n" + etoiles + "\n"

    return renduTitre


def afficheLignes(regex: str, lignes: list):
    renduLignes = ""
    lignesTrouvees = []

    for ligne in lignes:
        if re.search(regex, ligne):
            lignesTrouvees.append(ligne)

    for ligne in lignesTrouvees:
        renduLignes = renduLignes + ligne

    renduLignes = renduLignes + "*"*5 + " " + str(len(lignesTrouvees)) + " lignes trouvees " + "*"*5 + "\n\n"

    return renduLignes


def GenererFichier(nomFichier, sortieFichier):
    regexList = [
        r'[A-Z0-9]', 
        r'\.', 
        r'\.\.\.',
        r'(\s|)([0-9A-Fa-f])+(\s)', 
        r'(\s)*(([0-9A-Z])|([0-9a-z])){12,}(\s)*',
        r'([^a]*a){5,5}', 
        r'[\[|\]]', 
        r'^((a+)|(\s+))', 
        r'(([0-9]+)(\.)([0-9]+)(\.)([0-9]+)(\.)([0-9]+))',
        r'^(?![\s\S])',
        r'^(\s+)$',
        r'.',
        r'^((?!a).)*$',
        r'^((?! ).)*$',
        r'^((?![0-9]+).)*$',
        r'^(([0-9]{2})(\ )([0-9]{2})(\ )([0-9]{2})(\ )([0-9]{2})(\ )([0-9]{2}))',
        r'^(([0-9]{2})(\ |\-|\.)([0-9]{2})(\ |\-|\.)([0-9]{2})(\ |\-|\.)([0-9]{2})(\ |\-|\.)([0-9]{2}))',
        r'^(([0]|\(0\))([0-9]{1})(\ |\-|\.)([0-9]{2})(\ |\-|\.)([0-9]{2})(\ |\-|\.)([0-9]{2})(\ |\-|\.)([0-9]{2}))',
        r'(([0]|\(0\))(\ |\-|\.)([0-9]{3})(\ |\-|\.)([0-9]{3})(\ |\-|\.)([0-9]{3}))$'
    ]

    titreList = [
        "1.a: lignes contenant des chiffres ou des majuscules",
        "1.b: lignes contenant des points",
        "1.c: lignes contenant trois points",
        "1.d: lignes contenant des nombres hexadecimaux separes par des blancs",
        "1.e: lignes contenant un mot d'au moins 12 caracteres alphanumeriques",
        "1.f: lignes contenant exactement 5 lettres a(pas nécessairement successives)",
        "1.g: lignes contenant des crochets(] ou[)",
        "1.h: lignes ne contenant que des lettres a et des espaces",
        "1.i: lignes contenant quelque chose qui ressemble a une adresse IP",
        "2.a: lignes vides",
        "2.b: lignes blanches",
        "2.c: lignes non vides",
        "3.a: lignes qui ne contiennent pas de a",
        "3.b: lignes qui ne contiennent pas des espaces",
        "3.c: lignes qui ne contiennent pas des chiffres décimaux",
        "4: lignes qui débutent par un numéro de téléphone au format 01 23 45 67 89",
        "5: idem 4 mais on peut avoir . ou - a la place des espaces",
        "6: idem 5 mais le 0 peut être entoure de parentheses",
        "7: terminent par un tel au format 0 123 456 789, espaces, - ou . et(0)"
    ]

    sortieFichier.write(afficheTitre("PYTHON : Fichier de sortie de l'exercice 2 du TP4"))

    for i in range(0, len(regexList)):
        entreFichier = open(nomFichier, 'r')
        sortieFichier.write(afficheTitre(titreList[i]))
        sortieFichier.write(afficheLignes(regexList[i], entreFichier))
        entreFichier.close()


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

    outputFichier = open(output, 'w')
    GenererFichier(filename, outputFichier)
    outputFichier.close()


if __name__ == "__main__":
    main()  # Appel de notre fonction principale
    au_revoir()  # Appel de notre fonction pour quitter le programme
