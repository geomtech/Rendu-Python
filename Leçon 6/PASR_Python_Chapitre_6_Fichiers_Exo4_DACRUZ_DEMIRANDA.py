#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Auteur(s) : Dylan DE MIRANDA (dylandemiranda@gmail.com) & Alexy DA CRUZ (adacruz@geomtech.fr)
# Version : 0.1
# Date : 04/02/2021
# Thème du script : Analyse récursive des fichiers d'un répertoire

import os
import time

def goodBye():
    """
    affiche 3 sauts de ligne et Fin du programme
    Entrées : aucune
    Sortie : aucune
    """
    print("\n\n\nAu revoir\n\nFin du programme")

def analyseFile(file_path, word_to_find):
    """
    """
    if (os.path.exists(file_path)):
        word_founded = False
        lines_with_word = []

        try: # On essaie
            f = open(file_path, 'r', encoding="utf-8") # On ouvre le fichier demandé
            file_lines = f.readlines() # On liste les lignes

            lines_counter = 1 # On créer un compteur à partir de 1 car un fichier n'a pas de ligne 0 :-)
            for line in file_lines: # Pour chaque ligne du fichier
                if line.startswith(word_to_find): # SI la ligne commence par le mot recherché                    
                    line_str = str(lines_counter) + ":" + line
                    lines_with_word.append(line_str)
                    word_founded = True
                
                lines_counter += 1 # On compte les lignes
        except IOError: # Si une erreur de type IO survient
            print("Erreur : Le fichier", file_path, "n'est pas accessible") # On affiche un message d'erreur
        finally:
            f.close() # On ferme le fichier

        return [word_founded, lines_with_word]

def analyseDirectory(report_file, directory_path, word_to_find):
    """
    """
    directory_content = os.listdir(directory_path) # On liste les fichiers

    for content in directory_content: # Pour chaque fichier ou répertoire dans le répertoire
        content_path = os.path.join(directory_path, content)

        if (os.path.isfile(content_path)): # Si c'est un fichier
            result_analyse = analyseFile(content_path, word_to_find) # On analyse le fichier

            if (result_analyse[0]):
                directory_str = "Dossier : " + directory_path + "\n"
                filename_str = "\n" + str(os.path.basename(content_path)) + "\n"
                report_file.write(directory_str)
                report_file.write(filename_str)
                
                for line in result_analyse[1]:
                    if (line == result_analyse[1][-1]):
                        line_str = line + "\n"
                        report_file.write(line_str)
                    else:
                        report_file.write(line)
        elif (os.path.isdir(content_path)): # Si c'est un répertoire
            analyseDirectory(report_file, content_path, word_to_find) # On analyse le répertoire

################################################
############### MAIN PROGRAM  ##################
################################################

directory_to_analyse = input("Répertoire à analyser > ")
directory_path = os.path.join(os.getcwd(), directory_to_analyse)

if (os.path.exists(directory_path)):  # Si le répertoire existe
    word_to_find = input("Mot à trouver > ")    

    time_string_file = time.strftime("%d-%m-%Y-%H%M%S", time.localtime())
    time_string = "Date : " + str(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())) + "\n"
    report_filename = "report_" + str(time_string_file) + ".txt"

    report_file = open(report_filename, "w", encoding="utf-8")
    report_file.write(time_string)
    analyseDirectory(report_file, directory_path, word_to_find)
    report_file.close()
else:
    print("Ce répertoire n'existe pas")

goodBye()
