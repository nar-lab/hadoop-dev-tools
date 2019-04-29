#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

@author: Ali Cabukel
"""

import json
import os
from fs.config_parser import ConfigParser
from utils.global_vars import Globals
from err.file_logger import FileLogger
from err.exceptions import LogSettingFileNotFound, LogSettingFileNoContent


class LogSettingParser(object):

    def __init__(self):
        globalVars = Globals()
        self.__ROOT_DIR = globalVars.ROOT_DIR
        self.__RESOURCE_DIR = "resource"
        self.logger = FileLogger("logsettingreader")
        config_parser = ConfigParser()
        self.file_name = config_parser.get_config_value("logparser-param")

    def get_file_path(self):
        try:
            fp = os.path.join(self.__ROOT_DIR, self.__RESOURCE_DIR, self.file_name)
            if os.path.exists(fp):
                return fp
            else:
                raise LogSettingFileNotFound(self.file_name)
        except:
            raise

    def parse_settings(self):
        try:
            self.logger.info("Start Log Settings Parser")
            file_path = self.get_file_path()
            self.logger.debug("Read Log Settings File {0}".format(self.file_name))
            with open(file_path, "r") as fr:
                raw_data = fr.read()
                self.logger.debug("Parse Log Settings File {0}".format(self.file_name))
                r = raw_data.replace("\n", "").replace("\r", "")
                conf_json = json.loads(r)
                if len(conf_json) == 0:
                    raise LogSettingFileNoContent(self.file_name)
                self.logger.debug(
                    "Parse Completed {0}: File Content {1}".format(self.file_name, len(conf_json)))
                return conf_json
        except LogSettingFileNotFound:
            raise
        except LogSettingFileNoContent:
            raise
        except Exception as e:
            self.logger.error("Config File Parsing Error" + e)
            raise


