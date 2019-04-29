#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

parse edilecek log dosyasının okunmasını ve parse edilmesini sağlar
parse edilen dosya level, type ve contentlist şeklindedir

- constructor:
- get_file_path:
- read_log:
- parse_log:

@author: Ali Cabukel
"""

import os
from utils.global_vars import Globals
from utils.lambdas import Lambdas
from utils.funcs import Funcs
from err.file_logger import FileLogger
from err.exceptions import LogParserFileNotFound

class LogFileParser(object):

    def __init__(self, file_name):
        globalVars = Globals()
        self._IO_DIR = globalVars.IO_DIR
        self.logger = FileLogger("logparserreader")
        self.file_name = file_name
        self.lambdaFuncs = Lambdas()
        self.utilFuncs = Funcs()


    def get_file_path(self):
        try:
            fp = os.path.join(self._IO_DIR, self.file_name)
            if os.path.exists(fp):
                return fp
            else:
                raise LogParserFileNotFound(self.file_name)
        except:
            raise

    def read_log(self):
        try:
            file_path = self.get_file_path()
            with open(file_path, "r") as fr:
                raw_data = fr.readlines()
                return raw_data
        except LogParserFileNotFound:
            raise
        except:
            raise

    def parse_log(self):
        try:
            self.logger.info("Start Log Settings Parser")
            self.logger.debug("Read Log Settings File {0}".format(self.file_name))
            log_lines = self.read_log()
            self.logger.debug("Find Log File Pattern Sqoop / Bee")
            log_filtered_lines = list(filter(self.lambdaFuncs.fn_sqoop_filter_lines, log_lines))
            if len(log_filtered_lines) > 0 :
                log_splitted_lines = list(map(self.lambdaFuncs.fn_sqoop_splitter, log_filtered_lines))
                return [self.utilFuncs.loglines2dict_sqoop(x) for x in log_splitted_lines]
            else:
                log_filtered_lines = list(filter(self.lambdaFuncs.fn_bee_filter_lines, log_lines))
                if len(log_filtered_lines) > 2:
                  log_splitted_lines = list(map(self.lambdaFuncs.fn_bee_splitter, log_filtered_lines))
                  return [self.utilFuncs.loglines2dict_bee(x) for x in log_splitted_lines]
                else:
                  log_filtered_lines = list(filter(self.lambdaFuncs.fn_hive_filter_lines, log_lines))
                  log_splitted_lines = list(map(self.lambdaFuncs.fn_hive_splitter, log_filtered_lines))
                  return [self.utilFuncs.loglines2dict_hive(x) for x in log_splitted_lines]
        except Exception as e:
            self.logger.error("Config File Parsing Exception" + e)
            raise

