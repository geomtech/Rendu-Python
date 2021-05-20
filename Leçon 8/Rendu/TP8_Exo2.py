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


def afficheTitre(titre: str, titreRapport: bool = False):
    """
    génère un titre pour chaque étape ou pour le rapport avec une ligne d'étoiles
    avant et après de la longueur du titre
    Entrées : 
        titre        : titre de l'étape ou du rapport
        titreRapport : par défaut sur false, true si il s'agit du titre principal pour le rapport
    Sorties : 
        retourne une chaine de caractère avec le titre et les étoiles ainsi
        qu'un saut de ligne si il s'agit du titre du rapport
    """
    # Récupère la longueur du titre (nombre de caractères)
    longueurTitre = len(titre)
    # Génère un string contenant le bon nombre d'étoiles
    etoiles = "*"*longueurTitre
    # Génère le string contenant le titre et les étoiles
    renduTitre = etoiles + "\n" + titre + "\n" + etoiles + "\n"

    # Retourne le string généré
    return renduTitre


def afficheLignes(regex: str, lignes: list):
    """
    génère une liste des lignes trouvées par rapport aux regex appliqués
    Entrées :
        regex : filtre regex à appliquer sur la ligne
    Sorties :
        retourne une liste contenant les lignes trouvées par rapport aux regex appliqués 
    """
    renduLignes = ""
    lignesTrouvees = []

    # Pour chaque ligne du fichier
    for ligne in lignes:
        # On test le regex sur la ligne
        if re.search(regex, ligne):
            # Si ça match dans la ligne, on l'ajoute à la liste des lignes trouvées
            lignesTrouvees.append(ligne)

    # pour chaque ligne trouvée
    for ligne in lignesTrouvees:
        # On les ajoutes à la suite dans une chaine de caractères
        renduLignes = renduLignes + ligne

    # On ajoute ensuite le compte de lignes trouvées pour l'étape dans le rapport
    renduLignes = renduLignes + "*"*5 + " " + str(len(lignesTrouvees)) + " lignes trouvees " + "*"*5 + "\n\n"

    # On retourne la liste contenant les lignées trouvées
    return renduLignes

def GenererFichier(nomFichier, sortieFichier):
    """
    prend le fichier de base et applique des filtres regex
    sur chaque ligne et sort un fichier de sortie en tant
    que rapport sur les filtres regex appliqués
    Entrées :
        nomFichier    : nom du fichier de base dans lequel appliquer les filtres regex
        sortieFichier : fichier dans lequel écrire le rapport
    Sorties : aucune
    """

    # Liste contenant les regex à appliquer sur chaque ligne
    regexList = [
        r'[A-Z0-9]',  # 1.a: lignes contenant des chiffres ou des majuscules
        r'\.',  # 1.b: lignes contenant des points
        r'\.\.\.', # 1.c: lignes contenant trois points
        r'(\s|)([0-9A-Fa-f])+(\s)',  # 1.d: lignes contenant des nombres hexadecimaux separes par des blancs
        r'(\s)*(([0-9A-Z])|([0-9a-z])){12,}(\s)*', # 1.e: lignes contenant un mot d'au moins 12 caracteres alphanumeriques
        r'^(([^a]*?)(a)([^a]*?)){5}$', # 1.f: lignes contenant exactement 5 lettres a(pas nécessairement successives)
        r'[\[|\]]',  # 1.g: lignes contenant des crochets(] ou[)
        r'^((a+)|( ))',  # 1.h: lignes ne contenant que des lettres a et des espaces
        r'(([0-9]+)(\.)([0-9]+)(\.)([0-9]+)(\.)([0-9]+))', # 1.i: lignes contenant quelque chose qui ressemble a une adresse IP
        r'^\n$', # 2.a: lignes vides
        r'^(\s)+\n$', # 2.b: lignes blanches
        r'.', # 2.c: lignes non vides
        r'^((?!a).)*$', # 3.a: lignes qui ne contiennent pas de a
        r'^((?! ).)*$', # 3.b: lignes qui ne contiennent pas des espaces
        r'^((?![0-9]+).)*$', # 3.c: lignes qui ne contiennent pas des chiffres décimaux
        r'^(([0-9]{2})(\ )([0-9]{2})(\ )([0-9]{2})(\ )([0-9]{2})(\ )([0-9]{2}))', # 4: lignes qui débutent par un numéro de téléphone au format 01 23 45 67 89
        r'^(([0-9]{2})(\ |\-|\.)([0-9]{2})(\ |\-|\.)([0-9]{2})(\ |\-|\.)([0-9]{2})(\ |\-|\.)([0-9]{2}))', # 5: idem 4 mais on peut avoir . ou - a la place des espaces
        r'^(([0]|\(0\))([0-9]{1})(\ |\-|\.)([0-9]{2})(\ |\-|\.)([0-9]{2})(\ |\-|\.)([0-9]{2})(\ |\-|\.)([0-9]{2}))', # 6: idem 5 mais le 0 peut être entoure de parentheses
        r'(([0]|\(0\))(\ |\-|\.)([0-9]{3})(\ |\-|\.)([0-9]{3})(\ |\-|\.)([0-9]{3}))$' # 7: terminent par un tel au format 0 123 456 789, espaces, - ou . et(0
    ]

    # Liste des titres de chaque étape du rapport
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

    # Titre du rapport
    sortieFichier.write(afficheTitre("PYTHON : Fichier de sortie de l'exercice 2 du TP4"))

    # Pour chaque regex qui se trouve dans la liste
    for i in range(0, len(regexList)):
        # On ouvre le fichier de base en lecture
        entreFichier = open(nomFichier, 'r')
        # On écrit dans le fichier de sortie le titre de l'étape du rapport
        sortieFichier.write(afficheTitre(titreList[i]))
        # On écrit dans le fichier de sortie le rendu appliqué après le filtre regex
        sortieFichier.write(afficheLignes(regexList[i], entreFichier))
        # On ferme le fichier
        entreFichier.close()


################################################
########## PROGRAMME PRINCIPAL  ################
################################################

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

    # Ouvre le fichier de sortie en écriture
    outputFichier = open(output, 'w')
    # Appel de la fonction GenererFichier en renseignant le nom du fichier de base et en mettant l'objet file pour le fichier de sortie
    GenererFichier(filename, outputFichier)
    # Fermeture du fichier de sortie
    outputFichier.close()


if __name__ == "__main__":
    main()  # Appel de notre fonction principale
    au_revoir()  # Appel de notre fonction pour quitter le programme
