#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

@author: Ali Cabukel
"""

from string import Template
from utils.funcs import Funcs
from utils.sqoop_generator_templates import GeneratorTemplate

from fs.generator_parser import GeneratorParser
from fs.config_parser import ConfigParser
from fs.generator_writer import GeneratorWriter
from err.exceptions import GeneratorFileNoContent, GeneratorFileNotFound

class SqoopGenerator(object):

    def __init__(self, job_name):
        self.job_name = job_name
        self.file_ext = "txt"
        self.sqoop_stmt = ""
        self.utilFuncs = Funcs()

    def generate(self):
        try:
            genTemplates = GeneratorTemplate()
            genParser = GeneratorParser()
            obj_data = genParser.parse_generator(self.job_name)
            sqoop_args = self.fill_args(obj_data)
            if self.job_name == "__INIT__":
                sqoop_template = Template(genTemplates.basic_import_init())
                self.sqoop_stmt = sqoop_template.substitute(sqoop_args)
                self.file_ext = "txt"
            elif obj_data is None:
                sqoop_template = Template(genTemplates.basic_import_command())
                self.sqoop_stmt = sqoop_template.substitute(sqoop_args)
                self.file_ext = "sh"
            elif self.utilFuncs.get_generator_value(obj_data, "TEMPLATE")[0] == "BASIC_IMP_CMD":
                sqoop_template = Template(genTemplates.basic_import_command())
                self.sqoop_stmt = sqoop_template.substitute(sqoop_args)
                self.file_ext = "sh"
            elif self.utilFuncs.get_generator_value(obj_data, "TEMPLATE")[0] == "BASIC_IMP_OPT":
                sqoop_template = Template(genTemplates.basic_import_option_noinit())
                self.sqoop_stmt = sqoop_template.substitute(sqoop_args)
                self.file_ext = "txt"
            elif self.utilFuncs.get_generator_value(obj_data, "TEMPLATE")[0] == "BASIC_IMP_OPT_INIT":
                sqoop_template = Template(genTemplates.basic_import_option())
                self.sqoop_stmt = sqoop_template.substitute(sqoop_args)
                self.file_ext = "txt"
            elif self.utilFuncs.get_generator_value(obj_data, "TEMPLATE")[0] == "SPLIT_IMP_CMD":
                sqoop_template = Template(genTemplates.split_import_command())
                self.sqoop_stmt = sqoop_template.substitute(sqoop_args)
                self.file_ext = "sh"
            elif self.utilFuncs.get_generator_value(obj_data, "TEMPLATE")[0] == "SPLIT_IMP_OPT":
                sqoop_template = Template(genTemplates.split_import_option_noinit())
                self.sqoop_stmt = sqoop_template.substitute(sqoop_args)
                self.file_ext = "txt"
            elif self.utilFuncs.get_generator_value(obj_data, "TEMPLATE")[0] == "SPLIT_IMP_OPT_INIT":
                sqoop_template = Template(genTemplates.split_import_option())
                self.sqoop_stmt = sqoop_template.substitute(sqoop_args)
                self.file_ext = "txt"
            elif self.utilFuncs.get_generator_value(obj_data, "TEMPLATE")[0] == "DIRECT_IMP_CMD":
                sqoop_template = Template(genTemplates.direct_import_command())
                self.sqoop_stmt = sqoop_template.substitute(sqoop_args)
                self.file_ext = "sh"
            elif self.utilFuncs.get_generator_value(obj_data, "TEMPLATE")[0] == "DIRECT_IMP_OPT":
                sqoop_template = Template(genTemplates.direct_import_option_noinit())
                self.sqoop_stmt = sqoop_template.substitute(sqoop_args)
                self.file_ext = "txt"
            elif self.utilFuncs.get_generator_value(obj_data, "TEMPLATE")[0] == "DIRECT_IMP_OPT_INIT":
                sqoop_template = Template(genTemplates.direct_import_option())
                self.sqoop_stmt = sqoop_template.substitute(sqoop_args)
                self.file_ext = "txt"
            elif self.utilFuncs.get_generator_value(obj_data, "TEMPLATE")[0] == "BASIC_EXP_CMD":
                sqoop_template = Template(genTemplates.basic_export_command())
                self.sqoop_stmt = sqoop_template.substitute(sqoop_args)
                self.file_ext = "sh"
            else:
                sqoop_template = Template(genTemplates.basic_import_command())
                self.sqoop_stmt = sqoop_template.substitute(sqoop_args)
                self.file_ext = "sh"
        except (GeneratorFileNoContent, GeneratorFileNotFound):
            sqoop_template = Template(genTemplates.basic_import_command())
            self.sqoop_stmt = sqoop_template.substitute(sqoop_args)
            self.file_ext = "sh"
        finally:
            tmp_sqoop_stmt = self.sqoop_stmt
            genWriter = GeneratorWriter()
            genWriter.write2file(self.job_name, self.file_ext, self.sqoop_stmt)
            return(tmp_sqoop_stmt)


    def fill_args(self, obj_data):
        sqoop_args = dict()
        confParser = ConfigParser()
        sqoop_args["connstr"] = confParser.get_config_value("sqoop-conn-str")
        sqoop_args["username"] = confParser.get_config_value("db-user")
        sqoop_args["pwdfile"] = confParser.get_config_value("db-pass-file")
        sqoop_args["outdir"] = confParser.get_config_value("sqoop-out-dir")
        sqoop_args["tablename"] = self.job_name

        sqoop_args["targetdir"] = confParser.get_config_value("hdfs-root-path") + "/" + self.job_name
        if obj_data:
            if len(self.utilFuncs.get_generator_value(obj_data, "HDFS")) > 0:
                sqoop_args["targetdir"] = self.utilFuncs.get_generator_value(obj_data, "HDFS")[0]
                sqoop_args["exportdir"] = self.utilFuncs.get_generator_value(obj_data, "HDFS")[0]

        sqoop_args["fetchsize"] = 1000
        if obj_data:
            if len(self.utilFuncs.get_generator_value(obj_data, "FETCHSIZE")) > 0:
                sqoop_args["fetchsize"] = self.utilFuncs.get_generator_value(obj_data, "FETCHSIZE")[0]

        sqoop_args["nmappers"] = 20
        if obj_data:
            if len(self.utilFuncs.get_generator_value(obj_data, "NMAP")) > 0:
                sqoop_args["nmappers"] = self.utilFuncs.get_generator_value(obj_data, "NMAP")[0]

        sqoop_args["splitcol"] = "ID"
        if obj_data:
            if len(self.utilFuncs.get_generator_value(obj_data, "SPLITCOL")) > 0:
                sqoop_args["splitcol"] = self.utilFuncs.get_generator_value(obj_data, "SPLITCOL")[0]

        sqoop_args["mapredname"] = "sqoop_job_" + self.job_name

        return sqoop_args
