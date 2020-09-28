# !/usr/bin/python
# -*- coding: utf-8 -*-

from utilities import *
from constants import *


def slimer_script():
    backup_file = open(create_timestamped_and_named_file_name(SLIMER_SCRIPT_BACKUP_FILE_END_NAME,
                                                              APPLICATION_NAME), "w", encoding="utf-8")

    logging.info("SLIMER SCRIPT is currently running : creation of the backup file. "
                 "This can take up a few minutes...")

    for path in DIRECTORIES_TO_BE_SCANNED_FOR_BACKUP.values():
        backup_file.write("\nList of directories, subdirectories and descendants of the folder " + path + "\n")
        parse_directories(path, backup_file)
        backup_file.write("\n\n################################################################################ \n")
        backup_file.write("\nList of files in the folder " + path + "\n")
        parse_all_folders_and_files(path, backup_file)
        backup_file.write("\n\n################################################################################ \n")

    backup_file.close()
    logging.info("All paths have been scanned. The backup file is saved")
