#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

@author: Ali Cabukel
"""
from fs.config_parser import ConfigParser
import re

class Lambdas(object):

    def __init__(self):

        config_parser = ConfigParser()
        generator_file_sep = config_parser.get_config_value("generator-sep")
        self.fn_gen_splitter = lambda l: l.replace("\n", "").replace("\r", "").split(generator_file_sep)

        validator_file_sep = config_parser.get_config_value("validator-sep")
        self.fn_valid_splitter = lambda l: l.replace("\n", "").replace("\r", "").split(validator_file_sep)

        bee_pattern = re.compile(r"(INFO|ERROR|WARN|DEBUG)")
        self.fn_bee_filter_lines = lambda x: bee_pattern.match(x)

        sqoop_pattern = re.compile(r"^\d{2}\/\d{2}\/\d{2}\s\d{2}\:\d{2}\:\d{2}\s(INFO|ERROR|WARN|DEBUG)")
        self.fn_sqoop_filter_lines = lambda x: sqoop_pattern.match(x)

        hive_pattern = re.compile(r"^\d{2}\/\d{2}\/\d{2}\s\d{2}\:\d{2}\:\d{2}\s\[\w+")
        self.fn_hive_filter_lines = lambda x: hive_pattern.match(x)
        
        self.fn_sqoop_splitter = lambda x: x.split(": ")

        self.fn_bee_splitter = lambda x: x.split(": ")
        
        self.fn_hive_splitter = lambda x: x.split(": ")