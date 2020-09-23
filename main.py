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

from slimer_script import *
from alerts import *

timestamp = time.strftime("%Y%m%d") + "_" + time.strftime("%H%M%S")

logger_folder = create_timestamped_directory(SLIMER_SCRIPT_ROOT_APP_PATH, timestamp)

logger_setup(logger_folder, timestamp)

logging.info(SLIMER_SCRIPT_STARTING_MESSAGE)

try:
    slimer_script(timestamp)
    logging.info(SLIMER_SCRIPT_ENDING_MESSAGE)
except Exception as e:
    logging.error("The program ended unexpectedly !")
    logging.error("Error: " + str(e))

# logger_script()
#
# alm = Alerts()
# alm.run_script()
