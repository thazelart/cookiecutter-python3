#!/usr/bin/env python3
from utils.logger import Logger
from utils import args
import logging
import sys

#--------------------------------------------------------------------#
#                          GLOBAL VARIABLES                          #
#--------------------------------------------------------------------#


#--------------------------------------------------------------------#
#                               MAIN                                 #
#--------------------------------------------------------------------#
if __name__ == "__main__":
    # Parse arguments
    args = args.parseArguments()

    # Prepare the logger and write start log
    log = Logger()
    log.writer.info("Starting script")
    print("Change me !")
