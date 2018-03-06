#        .__  .__                                           .__        __
#   _____|  | |__| _____   ___________    ______ ___________|__|______/  |_
#  /  ___/  | |  |/     \_/ __ \_  __ \  /  ___// ___\_  __ \  \____ \   __\
#  \___ \|  |_|  |  Y Y  \  ___/|  | \/  \___ \\  \___|  | \/  |  |_> >  |
# /____  >____/__|__|_|  /\___  >__|    /____  >\___  >__|  |__|   __/|__|
#      \/              \/     \/             \/     \/         |__|

# Author :
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
# Python script tested on Windows 10. It can run on Unix OS with minor adjustements.


########################################################################################################################

########################################################################################################################

# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import shutil

# GLOBAL VARIABLES -----------------------------------------------------------------------------------------------------

# paths denotes a dictionnary of pathx representing...
# the directory(ies) pathx which you want to backup folders and files
# Add as many paths as directories which you want to backup the content
paths = {'path1': 'f:/'}

# file denotes the file in which you backup datas
# This file name will build by formatFileName() function
file = ''

# currentDirectory denotes the directory in which you will put the file file
currentDirectory = 'f:/Log'

# otherDirectories denotes a dictionnary of directories odx representing the directory(ies) odx...
# in which you want to put the backup file file, in addition to currentDirectory
# In this way, it's possible for example to put the backup file file in two differents hard drives
# In you don't want to use this feature, you must leave a pair of...
# ... one key + one value in the dictionnary otherDirectories, like this : otherDirectories = {'': ''}
otherDirectories = {'od1': 'c:/Log'}


# FUNCTIONS ------------------------------------------------------------------------------------------------------------

# Timestamping of the backup file name
def formatFileName():
    currentDate = time.strftime("%Y%m%d")
    currentTime = time.strftime("%H%M%S")
    formatFileName = currentDate + "_" + currentTime + "_log_slimerscript.txt"
    return formatFileName


# Parsing and displaying of folders, subfolders and descendants of the selectionned folder (path)
def parseDirs(path):
    nbDirectories = 0
    for root, dirs, files in os.walk(path):
        file.write("\n" + root)
        nbDirectories += 1
    file.write("\n\nnumber of folders in the directory " + path + " : " + str(nbDirectories - 1))


# Same as for the function parseDirs() + parsing and displaying of names' files
def parseAllFoldersAndFiles(path):
    nbFiles = 0
    for root, dirs, files in os.walk(path):
        file.write("\n" + root)
        for filename in files:
            # getsize() method must take into parameters the full path of a file, i.e. his root...
            # ... + his name. Join() method concatenate the two parameters
            # getsize() returns a result in octets, the result was divided by 1024 for convert in Ko, then we add...
            # ...  1 Ko for round up the result (Windows might make the same procedure for its explorer (?))
            size = (os.path.getsize(os.path.join(root, filename)) // 1024) + 1
            # getmtime() method returns the date of the file's last modification...
            # in the form of a timestamp
            timestamp = os.path.getmtime(os.path.join(root, filename))
            # timestamp conversion in the form of : DD/MM/YY HH:MM:SS
            timeFormatTemp = time.gmtime(timestamp)
            timeFormat = time.strftime("%x %X", timeFormatTemp)
            file.write("\n" + "--- " + filename + " *** " + timeFormat + " *** " + str(size) + " Ko")
            nbFiles += 1
    file.write("\n\nnumber of files in the directory " + path + " : " + str(nbFiles))


# SCRIPT ---------------------------------------------------------------------------------------------------------------

# If the work directory (the one which you should stock the file files) doesn't existe yet...
# ... creation of this directory
if not os.path.isdir(currentDirectory):
    os.makedirs(currentDirectory)

# Designation of the working directory as current directory
os.chdir(currentDirectory)

# Creating the file file + permission for the script to write in file
# It is necessary to add a parameter of encoding in UTF-8 if there is a place of the file tree...
# ... has a Japanese filename or any other "exotic" character set
file = open(formatFileName(), "w", encoding="utf-8")

print("SLIMER SCRIPT is currently running : creation of the backup file(s). "
      "This can take up to several minutes...")

# Write data in file file
for path in paths.values():
    file.write("\nList of directories, subdirectories and descendants of the folder " + path + "\n")
    parseDirs(path)
    file.write("\n\n################################################################################ \n")
    file.write("\nList of files of the folder " + path + "\n")
    parseAllFoldersAndFiles(path)
    file.write("\n\n################################################################################ \n")
    print("It's done !.")

# File file closure
file.close()

# Copying the file file to another backup directory (another hard drive for exemple)
if '' not in otherDirectories:
    for directory in otherDirectories.values():
        if not os.path.isdir(directory):
            os.makedirs(directory)
        os.chdir(directory)
        shutil.copy(currentDirectory + "/" + file.name, directory)

