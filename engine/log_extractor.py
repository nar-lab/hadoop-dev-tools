#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

@author: Ali Cabukel
"""

import re
from fs.logparser_setting_parser import LogSettingParser
from fs.logparser_parser import LogFileParser
from fs.logparser_writer import LogParserWriter

class LogExtractor(object):
    def __init__(self, log_file_name):
        self.log_file_name = log_file_name

    def extract_logs(self):
        try:
            logWriter = LogParserWriter()
            settingParser = LogSettingParser()
            fileParser = LogFileParser(file_name = self.log_file_name)
            all_matches = []
            for k,v in settingParser.parse_settings().items():
                ref_log_level = v["logLevel"]
                ref_log_type = v["logType"]
                ref_search_pattern = re.compile(v["searchPattern"])
                ref_extract_pattern = re.compile(v["extractPattern"])
                for el in fileParser.parse_log():
                    curr_log_level = el["log_level"]
                    curr_log_type = el["log_type"]
                    curr_log_details = el["log_details"]
                    if curr_log_level == ref_log_level and curr_log_type == ref_log_type:
                        for det in curr_log_details:
                            if ref_search_pattern.search(det):
                                knowledge_part = ref_search_pattern.search(det).group()
                                knowledge_part_loc = ref_search_pattern.search(det).span()
                                knowledge = ref_extract_pattern.search(knowledge_part).group()
                                all_matches.append([k, knowledge, knowledge_part_loc, v["searchPattern"]])
            logWriter.write2file(self.log_file_name,all_matches)
            return all_matches

        except:
            raise



