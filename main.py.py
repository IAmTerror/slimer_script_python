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


# !/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import shutil
from utilities import *
from constants import *

# GLOBAL VARIABLES -----------------------------------------------------------------------------------------------------





# FUNCTIONS ------------------------------------------------------------------------------------------------------------




# SCRIPT ---------------------------------------------------------------------------------------------------------------

if not os.path.isdir(BACKUP_FOLDER):
    os.makedirs(BACKUP_FOLDER)

# Designation of the working directory as current directory
os.chdir(BACKUP_FOLDER)

LOG_FILE = open(formatFileName(), "w", encoding="utf-8")

print("SLIMER SCRIPT is currently running : creation of the backup file(s). "
      "This can take up to several minutes...")

for path in DIRECTORIES_TO_BACKUP.values():
    LOG_FILE.write("\nList of directories, subdirectories and descendants of the folder " + path + "\n")
    parseDirs(path)
    LOG_FILE.write("\n\n################################################################################ \n")
    LOG_FILE.write("\nList of files of the folder " + path + "\n")
    parseAllFoldersAndFiles(path)
    LOG_FILE.write("\n\n################################################################################ \n")

LOG_FILE.close()
print("It's done !.")
