#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

@author: Ali Cabukel
"""

import logging
import os
from utils.global_vars import Globals
class FileLogger(object):

    def __init__(self, log_name = "bda_logs", log_file_name = "bda.log"):
        globalVars = Globals()
        self.__ROOT_DIR = globalVars.LOG_DIR
        log_file = os.path.join(self.__ROOT_DIR, log_file_name)
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s: %(levelname)s: %(name)s: %(message)s',
                            filename=log_file,
                            filemode='a')
        file = logging.FileHandler(log_file)
        file.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
        file.setFormatter(formatter)
        self.logger = logging.getLogger(log_name)
        self.logger.addHandler(file)

    def error(self, message):
        self.logger.error(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(message)

    def debug(self, message):
        self.logger.debug(message)