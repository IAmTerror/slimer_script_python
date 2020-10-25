# Slimer Script

<p align="center">
  <img src="https://raw.githubusercontent.com/IAmTerror/slimer_script_python/master/img/slimer.png" />
</p>

[![GNU GPL v3.0](https://img.shields.io/badge/licence-GNU%20GPL%20v3.0-blue)](https://github.com/IAmTerror/phoenix_down_script/blob/master/LICENSE) ![python v3.6](https://img.shields.io/badge/python-v3.6-blue)

Slimer Script is a script written in Python whose goal is to parse all the files on a hard disk, in order to collect their name, their size, and their last modification date.

These data are then saved as log files, saved locally, and uploaded to a server.

In case of a script execution error, a Trello alert is generated.

## Why I developed Phoenix Down Script ?

Because I'm a man a little paranoid. If one of my many hard drives decides to die, this script probably won't be able to resurrect it, but at least I'll know immediately which files need to be restored.

## How to run Phoenix Down Script ?

1. copy `constants_example.py` and `credentials_example.py` in `slimer_script/example` folder and paste them into the root of the application 
2. rename `constants_example.py` and `credentials_example.py` respectively into `constants.py` and `credentials.py` 
3. set values into `constants.py` and `credentials.py` ("Configuration variables", follow the instructions inside them)
4. In `main.py`, comment the following lines if you don't want to receive alerts on your Trello in case of bad script execution (or, if you don't know how to configure this service)

    ```
    alm = Alerts()
    alm.run_script()
    ```

5. In `main.py`, comment the following lines if you don't want to upload to a server the application's operating log (logger)
    ```
    logger_script()
    ```

6. In `slimer_script.py`, comment the following lines if you don't want to upload to a server the backup file of your hard drives or directories information
    ```
    upload_slimer_script_log(backup_file)
    ```
   
7. Create on your server (if you want to make a remote backup of your logs) a directory at your convenience for the Phoenix Down Script application (depending on the paths you set in step 3). In this directory you have to create a `log/slimer_script` folder. Then inside the `log/slimer_script` folder, you need to create a `logger` sub-folder ;

8. Do the same on your computer (or any other storage medium) for local backup (depending on the paths you set in step 3).
    
9. Run `main.py` ! Additional information : Slimer Script is above all intended to be executed automatically by your OS, via your task scheduler if you are on Windows, or `crontab` if you are on Linux.

During the execution of Slimer Script, some non-critical errors may occur. These may be for example exceptions due to the inability to read certain files (insufficient rights, etc...). These errors will not prevent the script from executing properly.

Warning : the execution of Slimer Script may take several minutes if you choose to parse one or more hard disks in their entirety. Please be patient !

<p align="center">
  <img src="https://raw.githubusercontent.com/IAmTerror/slimer_script_python/master/img/ghostbusters_logo.png" />
</p>

