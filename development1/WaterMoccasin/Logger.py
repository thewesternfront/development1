#!/usr/bin/python

"""
Author: Troy West
Date: 3/18/2019
Purpose: Log important game events to a file, supporting various logging levels
"""

import logging


class Logger:
    # Keep teh DEBUG level as the default.  This allows all other levels to be easily logged.
    default_logging_level = 'DEBUG'

    def __init__(self):
        logging.basicConfig(filename='/Users/cymruclan/Desktop/gamedata.log', filemode='a',
                            format='%(asctime)s \t %(name)s \t %(levelname)s \t %(message)s',
                            level=logging.DEBUG, datefmt='%d-%b-%y %H:%M:%S')

    def logEvent(self, log_event: object, log_level: object) -> object:

        if log_level == 'WARNING':
            logging.warning(log_event)
        elif log_level == 'DEBUG':
            logging.debug(log_event)
        elif log_level == 'INFO':
            logging.info(log_event)
        else:
            print("Error, logging level not found")
