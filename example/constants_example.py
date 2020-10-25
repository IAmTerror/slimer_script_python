# !/usr/bin/python
# -*- coding: utf-8 -*-

# CONFIGURATION VARIABLES (Requires a choice by the user !) ------------------------------------------------------------

# Root of the disks or directories that you want to parse for data backup.
# You can add others, by adding path3, path4 keys...
# Unix example
DIRECTORIES_TO_BE_SCANNED_FOR_BACKUP = {'path1': '/home/toto/',
                                        'path2': '/'}
# Windows with NAS Synology example
# DIRECTORIES_TO_BE_SCANNED_FOR_BACKUP = {'path1': 'C:/',
#                                         'path2': 'D:/',
#                                         'path3': 'F:/',
#                                         'path4': r'\\Nas1\homes',
#                                         'path5': r'\\Nas1\music',
#                                         'path6': r'\\Nas1\photo',
#                                         'path7': r'\\Nas1\video'}

# Directory where you want to save (locally) your logs.
SLIMER_SCRIPT_ROOT_LOGS_PATH = '/******/******/log/slimer_script'
# Directory where you want to save (locally) the logs about the slimer script application activity.
SLIMER_SCRIPT_ROOT_LOGGER_PATH = '/******/******/log/slimer_script/logger'

# Examples of boards and Trello labels. Rename according to your own needs, or disable alerts.py if...
# ... you don't want to be alerted via Trello of a script execution error.
# Read the Trello API documentation for more information.
TRELLO_MBL_BOARD_ADMIN_LIST_ID = ""
TRELLO_ALERT_BOARD_ALERT_LIST_ID = ""
TRELLO_MBL_URGENT_CUSTOM_LABEL_ID = ""
TRELLO_ALERT_URGENT_CUSTOM_LABEL_ID = ""


# APPLICATION VARIABLES ------------------------------------------------------------------------------------------------

# Directories to be excluded from parsing. Some directories can indeed cause bugs during parsing.
# For example, under Linux, parsing some network disks (/run/user/***) can cause a freeze of the script execution...
# ... without raising an exception !
EXCLUDED_DIRECTORIES = ['run']

APPLICATION_NAME = "slimer_script"
LOGGER_SUBDIRECTORY_NAME = "logger"

LOGGER_FILE_END_NAME = "log.txt"
SLIMER_SCRIPT_BACKUP_FILE_END_NAME = "backup_file.txt"

SEEDBOX_ROOT_SLIMER_SCRIPT_PATH = "/******/log/slimer_script"

SLIMER_SCRIPT_STARTING_MESSAGE = 'Slimer Script started !'
SLIMER_SCRIPT_ENDING_MESSAGE = 'Slimer Script finished !'


