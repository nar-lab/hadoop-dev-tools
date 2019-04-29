#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

@author: Ali Cabukel
"""

def sqoop_decorate(new_line):
    def wrapper(func):
        def generate(*args, **kwargs):
            return "sqoop{0}{1}{0}".format(new_line * 2, func(*args, **kwargs))
        return generate
    return wrapper

def import_decorate(new_line):
    def wrapper(func):
        def generate(*args, **kwargs):
            #return "import " + new_line * 2 + func(*args, **kwargs) + new_line * 2
            return "import{0}{1}{0}".format(new_line * 2, func(*args, **kwargs))
        return generate
    return wrapper

def export_decorate(new_line):
    def wrapper(func):
        def generate(*args, **kwargs):
            return "export{0}{1}{2}".format(new_line, func(*args, **kwargs), new_line * 2)
        return generate
    return wrapper

def init_decorate(new_line):
    def wrapper(func):
        def generate(*args, **kwargs):
            return "--connect{0}$connstr{1}--username{0}$username{1}--password-file{0}$pwdfile{1}{2}{0}"\
                .format(new_line, new_line * 2,func(*args, **kwargs))
        return generate
    return wrapper

def single_mapper(new_line):
    def wrapper(func):
        def generate(*args, **kwargs):
            return "-m{0}1{1}{2}{1}".format(new_line, new_line * 2, func(*args, **kwargs))
        return generate
    return wrapper

def split_by_mapper(new_line):
    def wrapper(func):
        def generate(*args, **kwargs):
            return "--num-mappers{0}$nmappers{1}--split-by{0}$splitcol{1}{2}{0}"\
                .format(new_line, new_line * 2,func(*args, **kwargs))
            return cmd
        return generate
    return wrapper

def db_table(new_line):
    def wrapper(func):
        def generate(*args, **kwargs):
            return "--table{0}$tablename{1}{2}{0}".format(new_line, new_line * 2, func(*args, **kwargs))
        return generate
    return wrapper

def hdfs_path(new_line):
    def wrapper(func):
        def generate(*args, **kwargs):
            return "--target-dir{0}$targetdir{1}--delete-target-dir{1}{2}{0}".format(new_line,new_line * 2,func(*args, **kwargs))
        return generate
    return wrapper

def as_textfile(new_line):
    def wrapper(func):
        def generate(*args, **kwargs):
            return "--as-textfile{0}{1}{2}".format(new_line * 2, func(*args, **kwargs), new_line)
        return generate
    return wrapper

def fetch_size(new_line):
    def wrapper(func):
        def generate(*args, **kwargs):
            return "--fetch-size{0}$fetchsize{1}{2}{0}".format(new_line, new_line * 2, func(*args, **kwargs))
        return generate
    return wrapper

def delimiters(new_line):
    def wrapper(func):
        def generate(*args, **kwargs):
            return "--lines-terminated-by{0}'\\n'{1}--fields-terminated-by{0}'|'{1}--input-null-string{0}''{1}--input-null-non-string{0}''{1}{2}{0}"\
                .format(new_line, new_line * 2,func(*args, **kwargs))
        return generate
    return wrapper

def direct(new_line):
    def wrapper(func):
        def generate(*args, **kwargs):
            return "--direct{0}{1}--num-mappers{0}$nmappers{1}{2}"\
                .format(new_line, new_line * 2,func(*args, **kwargs))
        return generate
    return wrapper

def connreset(new_line):
    def wrapper(func):
        def generate(*args, **kwargs):
            return "-Djava.security.egd=file:/dev/../dev/urandom{0}{1}"\
                .format(new_line * 2,func(*args, **kwargs))
        return generate
    return wrapper

def exportdir(new_line):
    def wrapper(func):
        def generate(*args, **kwargs):
            return "--export-dir{0}$exportdir{1}{2}".format(new_line, new_line * 2, func(*args, **kwargs))
        return generate
    return wrapper