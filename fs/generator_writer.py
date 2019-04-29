#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

@author: Ali Cabukel
"""

import os
from utils.global_vars import Globals
from fs.config_parser import ConfigParser

class GeneratorWriter(object):

    def __init__(self, ):
        globalVars = Globals()
        self.__IO_DIR = globalVars.IO_DIR

    def write2file(self, job_name, file_ext, sqoop_stmt):
        try:
            obj_name = job_name
            if "." in job_name:
                obj_name = job_name.split(".")[1]
            confParser = ConfigParser()
            out_file_name = confParser.get_config_value("sqoop-out-file-pattern") % (obj_name) + "." + file_ext
            out_file_path = self.set_file_path(out_file_name)
            with open(out_file_path, "w") as fw:
                fw.write(sqoop_stmt)            
        except:
            raise

    def set_file_path(self, file_name):
        try:
            return os.path.join(self.__IO_DIR, file_name)
        except:
            raise