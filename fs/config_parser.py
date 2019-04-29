#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

Bu paket uygulama konfigurasyon dosyasının "app.conf"
okunmasını ve parse edilmesini sağlar

+ methodlar:
- constructor: konfigurasyon dosya ismi parametre olarak alınır
- get_file_parh: konfigurasyon dosya yolunu bulur eger dosya yok ise exception fırlatılır. ConfigFileNotFound
- parse_config: konfigurasyon dosyasının okunması ve json verisinin parse edilmesini sağlar
    geriye dictionary tipinde bir set döner
    eğer dosya var ama içeriği boş ise ConfigFileNoContent exception'ı fırlatılır
- get_config_value: konfigurasyon dosyasında bulunan json verisinde
    aranacak key'e karşılık gelen değerin seçilmesini sağlar
    engine method'ları bu methoda erişir
    eğer key bulunmuyorsa ConfigKeyNotFound exception'ı fırlatılır

@author: Ali Cabukel
"""

import json
import os
from utils.global_vars import Globals
from err.file_logger import FileLogger
from err.exceptions import ConfigFileNotFound, ConfigKeyNotFound

class ConfigParser(object):

    def __init__(self, file_name = "app.conf"):
        globalVars = Globals()
        self.__ROOT_DIR = globalVars.ROOT_DIR
        self.__RESOURCE_DIR = "resource"
        self.logger = FileLogger("configreader")
        self.file_name = file_name

    def get_file_path(self):
        try:
            fp = os.path.join(self.__ROOT_DIR, self.__RESOURCE_DIR, self.file_name)
            if os.path.exists(fp):
                return fp
            else:
                raise ConfigFileNotFound(self.file_name)
        except:
            raise


    def parse_config(self):
        try:
            self.logger.info("Start Config Parser")
            self.logger.debug("Set Config File Name {0}".format(self.file_name))
            file_path = self.get_file_path()
            self.logger.debug("Read Config File {0}".format(self.file_name))
            with open(file_path, "r") as fr:
                raw_data = fr.read()
                self.logger.debug("Parse Config File {0}".format(self.file_name))
                conf_json = json.loads(raw_data)
                self.logger.debug("Parse Completed {0}: File Content {1}".format(self.file_name, len(conf_json)))
            return conf_json
        except ConfigFileNotFound as e:
            raise
        except Exception as e:
            self.logger.error("Config File Parsing Error" + e)
            raise


    def get_config_value(self, key):
        try:
            config_dict = self.parse_config()
            if key not in config_dict.keys():
                raise ConfigKeyNotFound(key)
            return config_dict[key]
        except:
            raise
