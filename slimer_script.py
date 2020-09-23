# !/usr/bin/python
# -*- coding: utf-8 -*-

from utilities import *
from constants import *
from logger_setup import *


def slimer_script(timestamp):
    backup_file = open(create_timestamped_and_named_file_name(timestamp, SLIMER_SCRIPT_BACKUP_FILE_END_NAME,
                                                              APPLICATION_NAME), "w", encoding="utf-8")

    logging.info("SLIMER SCRIPT is currently running : creation of the backup file(s). "
                 "This can take up to several minutes...")

    # for path in DIRECTORIES_TO_BACKUP.values():
    #     backup_file.write("\nList of directories, subdirectories and descendants of the folder " + path + "\n")
    #     parse_directories(path)
    #     backup_file.write("\n\n################################################################################ \n")
    #     backup_file.write("\nList of files of the folder " + path + "\n")
    #     parse_all_folders_and_files(path)
    #     backup_file.write("\n\n################################################################################ \n")

    backup_file.close()
    logging.info("It's done !")
