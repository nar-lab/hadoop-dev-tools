#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

@author: Ali Cabukel
"""

from functools import wraps

def orasql(cond):
    def select_decorate(func):
        @wraps(func)
        def func_wrapper(self):
            cond_stmt = "1 = 1"
            if cond == "IS_NULL":
                cond_stmt = " {0} IS NULL ".format(self.ora_col)
            elif cond == "LSN":
                cond_stmt == "LSN_ID = 1"
            return "(SELECT {0} FROM {1}.{2} WHERE {3}) rdd".format(func(self), self.ora_sch, self.ora_tbl, cond_stmt)
        return func_wrapper
    return select_decorate

def hiveql(cond):
    def select_decorate(func):
        @wraps(func)
        def func_wrapper(self):
            cond_stmt = "1 = 1"
            if cond == "IS_NULL":
                cond_stmt = " {0} IS NULL ".format(self.hive_col)
            return "SELECT {0} FROM {1}.{2} WHERE {3} ".format(func(self), self.hive_sch, self.hive_tbl, cond_stmt)
        return func_wrapper
    return select_decorate

def oragrp(cond):
    def group_decorate(func):
        @wraps(func)
        def func_wrapper(self):
            cond_stmt = "1 = 1"
            if cond == "IS_NULL":
                cond_stmt = " {0} IS NULL ".format(self.hive_col)
            return "(SELECT {0} FROM {1}.{2} WHERE {3} GROUP BY {4}) rdd".format(func(self), self.ora_sch, self.ora_tbl, cond_stmt, self.ora_col)
        return func_wrapper
    return group_decorate

def hivegrp(cond):
    def group_decorate(func):
        @wraps(func)
        def func_wrapper(self):
            cond_stmt = "1 = 1"
            if cond == "IS_NULL":
                cond_stmt = " {0} IS NULL ".format(self.hive_col)
            return "SELECT {0} FROM {1}.{2} WHERE {3} GROUP BY {4} ".format(func(self), self.hive_sch, self.hive_tbl, cond_stmt, self.hive_col)
        return func_wrapper
    return group_decorate