#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

sqoop generator uygulaması için gereken parametre dosyasının okunmasını ve parsae edilmesini sağlar

- constructor: konfigurasyon dosyası, global değişkenler ve util fonksiyonlar / lambda ifadeler
    etkinleştirilir
- get_file_path: parametre dosyasının path'ini ayarlar
- parse_generator: parametre dosyasının okunmasını sağlar
- parse_lines:  parametre dosyası satırlarının parse edilmesini sağlar


@author: Ali Cabukel
"""

import os
from fs.config_parser import ConfigParser
from utils.global_vars import Globals
from utils.funcs import Funcs
from utils.lambdas import Lambdas
from err.file_logger import FileLogger
from err.exceptions import GeneratorFileNotFound, GeneratorFileNoContent

class GeneratorParser(object):

    def __init__(self):
        globalVars = Globals()
        self.utilFuncs = Funcs()
        self.lambdaFuncs = Lambdas()
        config_parser = ConfigParser()
        self.logger = FileLogger("generatorreader")

        self.__ROOT_DIR, self.__RESOURCE_DIR = globalVars.ROOT_DIR, "resource"
        self.__GENERATOR_CONFIG_KEY = "generator-param"

        self.obj_sep = config_parser.get_config_value("generator-obj-sep")
        self.file_name = config_parser.get_config_value(self.__GENERATOR_CONFIG_KEY)

    def get_file_path(self, file_name):
        try:
            fp = os.path.join(self.__ROOT_DIR, self.__RESOURCE_DIR, file_name)
            if os.path.exists(fp):
                return fp
            else:
                raise GeneratorFileNotFound(file_name)
        except:
            raise

    def parse_generator(self, obj_name):
        try:
            self.logger.info("Start Generator Parser")
            file_path = self.get_file_path(self.file_name)
            self.logger.debug("Read Generator File {0}".format(self.file_name))
            with open(file_path, "r") as fr:
                raw_data = fr.readlines()
                self.logger.debug("Parse Generator File {0}".format(self.file_name))
                generator_objects = self.parse_lines(raw_data, self.obj_sep, obj_name)
                self.logger.debug("Parse Completed {0}: File Content {1}".format(self.file_name, len(generator_objects)))
            return generator_objects
        except GeneratorFileNotFound:
            return None
            raise
        except GeneratorFileNoContent:
            return None
            raise
        except Exception as e:
            return None
            self.logger.error("Generator File Reading Error" + e)
            raise

    def parse_lines(self, raw_lines, obj_sep, obj_name):
        try:
            file_lines = list(map(self.lambdaFuncs.fn_gen_splitter, raw_lines))
            filtered_lines = self.utilFuncs.map_generator_object(file_lines, obj_sep, obj_name)
            if len(filtered_lines) == 0:
                raise GeneratorFileNoContent(self.file_name)
            return filtered_lines
        except GeneratorFileNoContent:
            raise
        except:
            raise
