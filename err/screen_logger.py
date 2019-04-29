#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

@author: Ali Cabukel
"""

import logging

class ScreenLogger(logging.Logger):

    def __init__(self, log_name = "bda_logs"):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s: %(levelname)s: %(name)s: %(message)s',
                            #filename='myapp.log',
                            filemode='w')
        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s')
        console.setFormatter(formatter)
        self.logger = logging.getLogger(log_name)
        self.logger.addHandler(console)




    def error(self, message):
        self.logger.error(message)


    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(message)

    def debug(self, message):
        self.logger.debug(message)