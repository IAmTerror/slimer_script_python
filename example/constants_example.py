# !/usr/bin/python
# -*- coding: utf-8 -*-

APPLICATION_NAME = "slimer_script"
LOGGER_SUBDIRECTORY_NAME = "logger"

DIRECTORIES_TO_BE_SCANNED_FOR_BACKUP = {'path1': '/home/toto/',
                                        'path2': '/'}

SLIMER_SCRIPT_ROOT_LOGS_PATH = '/******/******/log/slimer_script'
SLIMER_SCRIPT_ROOT_LOGGER_PATH = '/******/******/log/slimer_script/logger'

LOGGER_FILE_END_NAME = "log.txt"
SLIMER_SCRIPT_BACKUP_FILE_END_NAME = "backup_file.txt"

SEEDBOX_ROOT_SLIMER_SCRIPT_PATH = "/******/log/slimer_script"

SLIMER_SCRIPT_STARTING_MESSAGE = 'Slimer Script started !'
SLIMER_SCRIPT_ENDING_MESSAGE = 'Slimer Script finished !'

# Examples of boards and Trello labels. Rename according to your own needs, or disable alerts.py if...
# ... you don't want to be alerted via Trello of a script execution error.
TRELLO_MBL_BOARD_ADMIN_LIST_ID = ""
TRELLO_ALERT_BOARD_ALERT_LIST_ID = ""
TRELLO_MBL_URGENT_CUSTOM_LABEL_ID = ""
TRELLO_ALERT_URGENT_CUSTOM_LABEL_ID = ""
