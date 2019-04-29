#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

@author: Ali Cabukel
"""
from utils.sqoop_gen_decorators import *

class GeneratorTemplate(object):

    def __init__(self):
        pass

    @import_decorate("\n")
    @connreset("\n")
    @init_decorate("\n")
    def basic_import_init(self):
        new_line = "\n"
        return "--verbose{0}--outdir{1}$outdir{0}".format(new_line * 2, new_line)

    @sqoop_decorate(" ")
    @import_decorate(" ")
    @init_decorate(" ")
    @single_mapper(" ")
    @db_table(" ")
    @hdfs_path(" ")
    @as_textfile(" ")
    @fetch_size(" ")
    @delimiters(" ")
    def basic_import_command(self):
        new_line = " "
        return "--mapreduce-job-name{0}$mapredname{1}".format(new_line, new_line * 2)

    @import_decorate("\n")
    @init_decorate("\n")
    @single_mapper("\n")
    @db_table("\n")
    @hdfs_path("\n")
    @as_textfile("\n")
    @fetch_size("\n")
    @delimiters("\n")
    def basic_import_option(self):
        new_line = "\n"
        return "--mapreduce-job-name{0}$mapredname{1}".format(new_line, new_line * 2)

    @single_mapper("\n")
    @db_table("\n")
    @hdfs_path("\n")
    @as_textfile("\n")
    @fetch_size("\n")
    @delimiters("\n")
    def basic_import_option_noinit(self):
        new_line = "\n"
        return "--mapreduce-job-name{0}$mapredname{1}".format(new_line, new_line * 2)

    @sqoop_decorate(" ")
    @import_decorate(" ")
    @init_decorate(" ")
    @split_by_mapper(" ")
    @db_table(" ")
    @hdfs_path(" ")
    @as_textfile(" ")
    @fetch_size(" ")
    @delimiters(" ")
    def split_import_command(self):
        new_line = " "
        return "--mapreduce-job-name{0}$mapredname{1}".format(new_line, new_line * 2)

    @import_decorate("\n")
    @init_decorate("\n")
    @split_by_mapper("\n")
    @db_table("\n")
    @hdfs_path("\n")
    @as_textfile("\n")
    @fetch_size("\n")
    @delimiters("\n")
    def split_import_option(self):
        new_line = "\n"
        return "--mapreduce-job-name{0}$mapredname{1}".format(new_line, new_line * 2)

    @split_by_mapper("\n")
    @db_table("\n")
    @hdfs_path("\n")
    @as_textfile("\n")
    @fetch_size("\n")
    @delimiters("\n")
    def split_import_option_noinit(self):
        new_line = "\n"
        return "--mapreduce-job-name{0}$mapredname{1}".format(new_line, new_line * 2)

    @sqoop_decorate(" ")
    @import_decorate(" ")
    @init_decorate(" ")
    @direct(" ")
    @db_table(" ")
    @hdfs_path(" ")
    @as_textfile(" ")
    @fetch_size(" ")
    @delimiters(" ")
    def direct_import_command(self):
        new_line = " "
        return "--mapreduce-job-name{0}$mapredname{1}".format(new_line, new_line * 2)

    @import_decorate("\n")
    @init_decorate("\n")
    @direct("\n")
    @db_table("\n")
    @hdfs_path("\n")
    @as_textfile("\n")
    @fetch_size("\n")
    @delimiters("\n")
    def direct_import_option(self):
        new_line = "\n"
        return "--mapreduce-job-name{0}$mapredname{1}".format(new_line, new_line * 2)

    @direct("\n")
    @db_table("\n")
    @hdfs_path("\n")
    @as_textfile("\n")
    @fetch_size("\n")
    @delimiters("\n")
    def direct_import_option_noinit(self):
        new_line = "\n"
        return "--mapreduce-job-name{0}$mapredname{1}".format(new_line, new_line * 2)

    @sqoop_decorate(" ")
    @export_decorate(" ")
    @init_decorate(" ")
    @single_mapper(" ")
    @db_table(" ")
    @exportdir(" ")
    @delimiters(" ")
    def basic_export_command(self):
        new_line = "\n"
        return "--mapreduce-job-name{0}$mapredname{1}".format(new_line, new_line * 2)


