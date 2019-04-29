#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

@author: Ali Cabukel
"""

import unittest
from fs.config_parser import ConfigParser

class ConfigReaderTest(unittest.TestCase):

    def test_config_file_name_invalid(self):
        config_parser_inst = ConfigParser("app1.conf")
        conf_json = config_parser_inst.get_file_path()
        self.failureException()

    def test_config_file_element_length(self):
        config_parser_inst = ConfigParser()
        conf_json = config_parser_inst.parse_config()
        conf_json_len = len(conf_json)
        self.assertEqual(conf_json_len, 7)

    def test_dbuser_exists(self):
        config_parser_inst = ConfigParser()
        db_user_name = config_parser_inst.get_config_value("db-user")
        self.assertIsNotNone(db_user_name)

    def test_get_db_pass(self):
        config_parser_inst = ConfigParser()
        db_password = config_parser_inst.get_config_value("db-pass")
        self.assertIsNotNone(db_password)

    def test_get_db_passfile(self):
        config_parser_inst = ConfigParser()
        db_pass_file = config_parser_inst.get_config_value("db-pass-file")
        self.assertIsNotNone(db_pass_file)

    def test_get_hdfs_root(self):
        config_parser_inst = ConfigParser()
        hdfs_root_path = config_parser_inst.get_config_value("hdfs-root-path")
        self.assertIsNotNone(hdfs_root_path)

    def test_get_validator_param(self):
        config_parser_inst = ConfigParser()
        validator_param = config_parser_inst.get_config_value("validator-param")
        self.assertEqual(validator_param, "validation-settings.txt")

    def test_get_logparser_param(self):
        config_parser_inst = ConfigParser()
        logparser_param = config_parser_inst.get_config_value("logparser-param")
        self.assertEqual(logparser_param, "logparser-settings.json")

    def test_get_logparser_param(self):
        config_parser_inst = ConfigParser()
        generator_param = config_parser_inst.get_config_value("generator-param")
        self.assertEqual(generator_param, "generator-settings.txt")


unittest.main()

