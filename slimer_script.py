#        .__  .__                                           .__        __
#   _____|  | |__| _____   ___________    ______ ___________|__|______/  |_
#  /  ___/  | |  |/     \_/ __ \_  __ \  /  ___// ___\_  __ \  \____ \   __\
#  \___ \|  |_|  |  Y Y  \  ___/|  | \/  \___ \\  \___|  | \/  |  |_> >  |
# /____  >____/__|__|_|  /\___  >__|    /____  >\___  >__|  |__|   __/|__|
#      \/              \/     \/             \/     \/         |__|

# Auteur :
# +-+-+-+-+-+-+-+-+-+
# |I|A|m|T|e|r|r|o|r|
# +-+-+-+-+-+-+-+-+-+

# Licence :
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

# Notes :
# Script testé sous Windows 10. Fonctionnement possible sous OS Unix sous réserve d'adaptations mineures du script.

########################################################################################################################

########################################################################################################################

# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import shutil

# VARIABLES GLOBALES ---------------------------------------------------------------------------------------------------

# paths designe un dictionnaire de pathx représentant...
# ... le ou les répertoire(s) pathx dont on veut sauvegarder les dossiers et les fichiers
# Ajoutez autant de paths que de répertoires dont on veut sauvegarder le contenu
paths = {'path1': 'f:/'}

# file designe le fichier dans lequel on sauvegardera les données
# Le nom de ce fichier sera crée grâce à la fonction formatFileName()
file = ''

# currentDirectory designe le repertoire dans lequel on placera le fichier file
currentDirectory = 'f:/Log'

# otherDirectories designe un dictionnaire de repertoires odx représentant le ou les répertoire(s) odx ...
# ... dans lesquels on veut placer notre fichier de sauvegarde file, en plus de currentDirectory
# Il est ainsi possible par exemple d'effectuer la sauvegarde du fichier file sur deux disques durs différents
# Si vous ne souhaitez pas utiliser cette fonctionnalité, il est nécessaire de...
# ... laisser un couple clé + valeur vide dans la variable otherDirectories : otherDirectories = {'': ''}
otherDirectories = {'od1': 'c:/Log'}


# FONCTIONS ------------------------------------------------------------------------------------------------------------

# Horodatage du nom de fichier de sauvegarde
def formatFileName():
    currentDate = time.strftime("%Y%m%d")
    currentTime = time.strftime("%H%M%S")
    formatFileName = currentDate + "_" + currentTime + "_log_slimerscript.txt"
    return formatFileName


# Parsing et affichage des répertoires, sous-répetoires et descendants du dossier sélectionné (path)
def parseDirs(path):
    nbDirectories = 0
    for root, dirs, files in os.walk(path):
        file.write("\n" + root)
        nbDirectories += 1
    file.write("\n\nNombre de dossiers dans le répertoire " + path + " : " + str(nbDirectories - 1))


# Même chose que pour la fonction parseDirs() + parsing et affichage des noms des fichiers
def parseAllFoldersAndFiles(path):
    nbFiles = 0
    for root, dirs, files in os.walk(path):
        file.write("\n" + root)
        for filename in files:
            # La méthode getsize() doit prendre en paramètre le chemin complet d'un fichier, c'est à dire sa racine...
            # ... + son nom, d'où l'utilisation de la méthode join pour concaténer les deux paramètres
            # getsize() renvoie un résultat en octets, on divise par 1024 pour convertir en ko...
            # ... puis on ajoute 1 ko pour arrondir au ko supérieur (c'est ce que semble aussi faire l'OS Windows (?))
            size = (os.path.getsize(os.path.join(root, filename)) // 1024) + 1
            # la methode getmtime() renvoie la date de la dernière modification d'un fichier...
            # ... sous la forme d'un timestamp
            timestamp = os.path.getmtime(os.path.join(root, filename))
            # conversion timestamp en une date sous la forme DD/MM/YY HH:MM:SS
            timeFormatTemp = time.gmtime(timestamp)
            timeFormat = time.strftime("%x %X", timeFormatTemp)
            file.write("\n" + "--- " + filename + " *** " + timeFormat + " *** " + str(size) + " Ko")
            nbFiles += 1
    file.write("\n\nNombre de fichiers dans le répertoire " + path + " : " + str(nbFiles))


# SCRIPT ---------------------------------------------------------------------------------------------------------------

# Si le répertoire de travail (celui dans lequel on souhaite stocker nos fichiers file) n'existe pas...
# ... création de ce répertoire
if not os.path.isdir(currentDirectory):
    os.makedirs(currentDirectory)

# Désignation du répertoire de travail comme répertoire courant
os.chdir(currentDirectory)

# Création du fichier file + permission pour le script d'écrire dans file
# Il est nécessaire d'ajouter un paramètre d'encodage en UTF-8 si a un endroit de l'arborescence de fichiers...
# ... se trouve un nom de fichier en caractères japonais ou tout autre jeu de caractères "exotiques"
file = open(formatFileName(), "w", encoding="utf-8")

# Ecriture des données nécessaires sur le fichier file
print("Exécution du script slimer_script: création du (ou des) fichier(s) de sauvegarde. "
      "Cette opération peut prendre jusqu'à plusieurs minutes...")

for path in paths.values():
    file.write("\nListe des répertoires, sous-répetoires et descendants du dossier " + path + "\n")
    parseDirs(path)
    file.write("\n\n################################################################################ \n")
    file.write("\nListe des répertoires, sous-répetoires et descendants du dossier " + path + "\n")
    parseAllFoldersAndFiles(path)
    file.write("\n\n################################################################################ \n")
    print("Script exécuté avec succès.")

# Fermeture du fichier file
file.close()

# Copie du fichier file dans un autre répertoire de sauvegarde (un autre disque dur par exemple)
if '' not in otherDirectories:
    for directory in otherDirectories.values():
        if not os.path.isdir(directory):
            os.makedirs(directory)
        os.chdir(directory)
        shutil.copy(currentDirectory + "/" + file.name, directory)

