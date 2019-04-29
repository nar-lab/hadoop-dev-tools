#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

- constructor:
- get_file_path:
- parse_validation:
- parse_lines
- find_validation_object

@author: Ali Cabukel
"""

import os
from fs.config_parser import ConfigParser
from utils.global_vars import Globals
from utils.funcs import Funcs
from utils.lambdas import Lambdas
from err.file_logger import FileLogger
from err.exceptions import ValidationNoContent, ValidationFileNotFound, ValidationObjectArgError, ValidationObjectNotFound

class ValidationParser(object):

    def __init__(self):
        globalVars = Globals()
        self.utilFunctions = Funcs()
        self.lambdaFuncs = Lambdas()
        self.__ROOT_DIR = globalVars.ROOT_DIR
        self.__RESOURCE_DIR = "resource"
        self.__VALIDATION_CONFIG_KEY = "validator-param"
        self.logger = FileLogger("validationreader")
        config_parser = ConfigParser()
        self.file_name = config_parser.get_config_value(self.__VALIDATION_CONFIG_KEY)
        self.obj_sep = config_parser.get_config_value("validator-sep")

    def get_file_path(self, file_name):
        try:
            fp = os.path.join(self.__ROOT_DIR, self.__RESOURCE_DIR, file_name)
            if os.path.exists(fp):
                return fp
            else:
                raise ValidationFileNotFound(file_name)
        except:
            raise

    def parse_validation(self):
        try:
            self.logger.info("Start Validation Parser")
            file_path = self.get_file_path(self.file_name)
            self.logger.debug("Read Validation File {0}".format(self.file_name))
            with open(file_path, "r") as fr:
                raw_data = fr.readlines()
                self.logger.debug("Parse Validation File {0}".format(self.file_name))
                validation_objects = self.parse_lines(raw_data, self.obj_sep)
                self.logger.debug("Parse Complete {0}: File Content {1}".format(self.file_name, len(validation_objects)))
            return validation_objects
        except ValidationFileNotFound as e:
            raise
        except ValidationNoContent:
            raise
        except:
            self.logger.error("Validation File Reading Error")
            raise

    def parse_lines(self, raw_lines, line_sep):
        try:
            file_lines = list(map(self.lambdaFuncs.fn_valid_splitter, raw_lines))
            header = file_lines[0]
            file_lines = file_lines[1:]
            mapped_lines = self.utilFunctions.map_validation_object(file_lines, header)
            if len(mapped_lines) == 0:
                raise ValidationNoContent(self.file_name)
            return mapped_lines
        except:
            raise

    def find_validation_object(self, **kwargs):
        object_map_list = self.parse_validation()
        if(len(kwargs) == 6):
            kwargs_str = self.utilFunctions.fn_dict_formatter(kwargs.items())
            db_object_list = []
            for o in object_map_list:
                obj_list = list(o.items())[:6]
                o_str = self.utilFunctions.fn_dict_formatter(obj_list)
                db_object_list.append(o_str)
            db_object_list = list(set(db_object_list))
            if kwargs_str in db_object_list:
                hive_obj = self.utilFunctions.fn_object_formatter(kwargs["HIVE_SCH"], kwargs["HIVE_TBL"], kwargs["HIVE_COL"])
                ora_obj = self.utilFunctions.fn_object_formatter(kwargs["ORA_SCH"], kwargs["ORA_TBL"], kwargs["ORA_COL"])
                return hive_obj, ora_obj
            else:
                raise ValidationObjectNotFound(kwargs_str)
        else:
            raise ValidationObjectArgError(len(kwargs))


