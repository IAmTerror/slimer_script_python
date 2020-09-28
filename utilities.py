# !/usr/bin/python
# -*- coding: utf-8 -*-

import time
import os
from constants import *
import logging


def create_directory(path):
    logging.info('creating the folder ' + path + "...")
    if not os.path.isdir(path):
        os.makedirs(path)
        logging.info("the folder " + path + " was successfully created")
    else:
        logging.info("the folder " + path + " already exists, it's ok")
    # Designation of the working directory as current directory
    os.chdir(path)


def create_timestamped_directory(path, timestamp):
    format_timestamped_subdirectory = path + "/" + timestamp
    logging.info('creating the folder ' + format_timestamped_subdirectory + "...")
    if not os.path.isdir(format_timestamped_subdirectory):
        os.makedirs(format_timestamped_subdirectory)
        logging.info("the folder " + format_timestamped_subdirectory + " was successfully created")
    else:
        logging.info("the folder " + format_timestamped_subdirectory + " already exists, it's ok")
    # Designation of the working directory as current directory
    os.chdir(format_timestamped_subdirectory)
    return format_timestamped_subdirectory


def create_timestamped_and_named_file_name(timestamp, file_name, application_name=None):
    format_file_name = timestamp + "_" + application_name + "_" + file_name
    return format_file_name


def parse_directories(path, backup_file):
    number_of_directories = 0
    for root, dirs, files in os.walk(path):
        backup_file.write("\n" + root)
        number_of_directories += 1
    backup_file.write("\n\nnumber of folders in the directory " + path + " : " + str(number_of_directories - 1))


def parse_all_folders_and_files(path, backup_file):
    number_of_files = 0
    for root, dirs, files in os.walk(path):
        backup_file.write("\n" + root)
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
            time_format_temp = time.gmtime(timestamp)
            time_format = time.strftime("%x %X", time_format_temp)
            backup_file.write("\n" + "--- " + filename + " *** " + time_format + " *** " + str(size) + " Ko")
            number_of_files += 1
    backup_file.write("\n\nnumber of files in the directory " + path + " : " + str(number_of_files))
