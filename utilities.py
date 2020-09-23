# !/usr/bin/python
# -*- coding: utf-8 -*-

import time
from constants import *


def formatFileName():
    currentDate = time.strftime("%Y%m%d")
    currentTime = time.strftime("%H%M%S")
    formatFileName = currentDate + "_" + currentTime + "_log_slimerscript.txt"
    return formatFileName


def parseDirs(path):
    nbDirectories = 0
    for root, dirs, files in os.walk(path):
        LOG_FILE.write("\n" + root)
        nbDirectories += 1
    LOG_FILE.write("\n\nnumber of folders in the directory " + path + " : " + str(nbDirectories - 1))


def parseAllFoldersAndFiles(path):
    nbFiles = 0
    for root, dirs, files in os.walk(path):
        LOG_FILE.write("\n" + root)
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
            LOG_FILE.write("\n" + "--- " + filename + " *** " + timeFormat + " *** " + str(size) + " Ko")
            nbFiles += 1
    LOG_FILE.write("\n\nnumber of files in the directory " + path + " : " + str(nbFiles))