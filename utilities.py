# !/usr/bin/python
# -*- coding: utf-8 -*-

import time
import os
from credentials import *
from constants import *
import logging
import ftplib
from ftplib import FTP


def create_directory(path):
    logging.info('creating the folder ' + path + "...")
    if not os.path.isdir(path):
        os.makedirs(path)
        logging.info("the folder " + path + " was successfully created")
    else:
        logging.info("the folder " + path + " already exists, it's ok")
    # Designation of the working directory as current directory
    os.chdir(path)


def create_timestamped_and_named_file_name(file_name, application_name=None):
    timestamp = time.strftime("%Y%m%d") + "_" + time.strftime("%H%M%S")
    format_file_name = timestamp + "_" + application_name + "_" + file_name
    return format_file_name


def parse_directories(path, backup_file):
    number_of_directories = 0
    for root, dirs, files in os.walk(path):
        backup_file.write("\n" + root)
        number_of_directories += 1
    backup_file.write("\n\nNumber of folders in the directory " + path + " : " + str(number_of_directories - 1))


def parse_all_folders_and_files(path, backup_file):
    number_of_files = 0
    for root, dirs, files in os.walk(path):
        files = [os.path.join(dirs, f) for f in files if not SLIMER_SCRIPT_FILES_EXCLUDED_FROM_PARSING]
        backup_file.write("\n" + root)
        for file in files:
            path_name = os.path.join(root, file)
            # getsize() method must take into parameters the full path of a file, i.e. his root...
            # ... + his name. Join() method concatenate the two parameters
            # getsize() returns a result in octets, the result was divided by 1024 for convert in Ko, then we add...
            # ...  1 Ko for round up the result (Windows might make the same procedure for its explorer (?))
            size = (os.path.getsize(os.path.join(root, path_name)) // 1024) + 1
            # getmtime() method returns the date of the file's last modification...
            # in the form of a timestamp
            timestamp = os.path.getmtime(os.path.join(root, path_name))
            # timestamp conversion in the form of : DD/MM/YY HH:MM:SS
            time_format_temp = time.gmtime(timestamp)
            time_format = time.strftime("%x %X", time_format_temp)
            backup_file.write("\n" + "--- " + path_name + " *** " + time_format + " *** " + str(size) + " Ko")
            number_of_files += 1
    backup_file.write("\n\nNumber of files in the directory " + path + " : " + str(number_of_files))


def get_the_latest_file_in_a_folder(path):
    list_of_files = os.listdir(path)  # get a list of all file names in a folder
    # get a list of absolute paths for previously recovered files
    paths = [os.path.join(path, basename) for basename in list_of_files]
    # return the latest (most recent modified metadata) file
    return max(paths, key=os.path.getctime)


def upload_file_to_server_ftp(file, filename):
    ftp = FTP(SEEDBOX_DOMAIN_NAME)  # connect to host, default port
    try:
        logging.info("trying to connect the ftp server...")
        ftp.login(user=SEEDBOX_USER_NAME, passwd=SEEDBOX_PASSWD)  # login with credentials
        logging.info('ftp connection succeed !')
        try:
            # TODO : se placer dans le bon repertoire (ok) du serveur et
            #  creer un dossier *nom application* s'il n'existe pas
            ftp.cwd(SEEDBOX_ROOT_SLIMER_SCRIPT_PATH)  # Set the current directory on the server
            logging.info('sending ' + filename + ' file to the ftp server...')
            ftp.storbinary('STOR ' + filename + '', file)  # uploading file to the server
            logging.info(filename + ' uploaded successfully!')
        except ftplib.all_errors:
            logging.error('unable to make directories')
    except ftplib.all_errors:
        logging.error('unable to connect to ftp server')
    ftp.quit()


def upload_file_to_server_ftp_without_logging_messages(file, filename, subdirectory):
    ftp = FTP(SEEDBOX_DOMAIN_NAME)  # connect to host, default port
    try:
        print("trying to connect the ftp server...")
        ftp.login(user=SEEDBOX_USER_NAME, passwd=SEEDBOX_PASSWD)  # login with credentials
        print('ftp connection succeed !')
        try:
            # TODO : se placer dans le bon repertoire (ok) du serveur et
            #  creer un dossier *nom application* s'il n'existe pas
            ftp.cwd(SEEDBOX_ROOT_SLIMER_SCRIPT_PATH + "/" + subdirectory)  # Set the current directory on the server
            print('sending ' + filename + ' file to the ftp server... (' + subdirectory + ' file)')
            ftp.storbinary('STOR ' + filename + '', file)  # uploading file to the server
            print(filename + ' uploaded successfully!')
        except ftplib.all_errors:
            print('unable to make directories')
    except ftplib.all_errors:
        print('unable to connect to ftp server')
    ftp.quit()
