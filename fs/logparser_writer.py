#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

@author: Ali Cabukel
"""
import os
from utils.global_vars import Globals
import datetime
class LogParserWriter(object):

    def __init__(self, ):
        globalVars = Globals()
        self.__IO_DIR = globalVars.IO_DIR

    def write2file(self, log_file_name, output):
        try:
            out_file_path = self.set_file_path("log-out.txt")
            with open(out_file_path, "a") as fw:
                for o in output:
                    fw.writelines(log_file_name + " - " + str(datetime.datetime.now()) + ": "+ str(o) + "\n")
        except:
            raise

    def set_file_path(self, file_name):
        try:
            return os.path.join(self.__IO_DIR, file_name)
        except:
            raise