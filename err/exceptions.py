#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

@author: Ali Cabukel
"""

from err.screen_logger import ScreenLogger

class BdaException(Exception):
    logger = ScreenLogger("exceptions")

class ConfigFileNotFound(BdaException):
    def __init__(self, message = ""):
        self.message = super().logger.error("Config File Not Found: {0}".format(message))

class ConfigKeyNotFound(BdaException):
    def __init__(self, message = ""):
        self.message = super().logger.error("Config Key Not Found: {0}".format(message))

class ValidationFileNotFound(BdaException):
    def __init__(self, message = ""):
        self.message = super().logger.error("Validation File Not Found: {0}".format(message))

class ValidationNoContent(BdaException):
    def __init__(self, message = ""):
        self.message = super().logger.error("Validation File Has No Content: {0}".format(message))

class ValidationObjectNotFound(BdaException):
    def __init__(self, message = ""):
        self.message = super().logger.error("Validation Object Not Found: {0}".format(message))

class ValidationObjectArgError(BdaException):
    def __init__(self, message = ""):
        self.message = super().logger.error("Validation Object Argument Problem: {0}".format(message))


class GeneratorFileNotFound(BdaException):
    def __init__(self, message = ""):
        self.message = super().logger.error("Generator File Not Found: {0}".format(message))

class GeneratorFileNoContent(BdaException):
    def __init__(self, message = ""):
        self.message = super().logger.error("Generator File Has No Content: {0}".format(message))

class LogSettingFileNotFound(BdaException):
    def __init__(self, message = ""):
        self.message = super().logger.error("Log Settings File Not Found: {0}".format(message))

class LogSettingFileNoContent(BdaException):
    def __init__(self, message = ""):
        self.message = super().logger.error("Log Settings File Has No Content: {0}".format(message))

class LogParserFileNotFound(BdaException):
    def __init__(self, message = ""):
        self.message = super().logger.error("Log Parser File Not Found: {0}".format(message))
