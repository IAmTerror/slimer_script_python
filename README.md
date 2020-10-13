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
3. set values into `constants.py` and `credentials.py` (follow the instructions inside them)
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
    
7. Run main.py !

<p align="center">
  <img src="https://raw.githubusercontent.com/IAmTerror/slimer_script_python/master/img/ghostbusters_logo.png" />
</p>

