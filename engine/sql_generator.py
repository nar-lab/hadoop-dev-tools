#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

@author: Ali Cabukel
"""

from fs.validation_parser import ValidationParser
from utils.sql_gen_decorators import *

class ValidationSQLGenerator(object):

    def __init__(self):
        valid = ValidationParser()
        hive_obj, ora_obj = valid.find_validation_object(
                        HIVE_SCH="BERKA_DB",
                        HIVE_TBL="BERKA_TBL",
                        HIVE_COL="BERKA_COL",
                        ORA_SCH="DB_BERKA_DB",
                        ORA_TBL="DB_BERKA_TBL",
                        ORA_COL="DB_BERKA_COL")
        self.hive_sch = hive_obj.split(".")[0]
        self.hive_tbl = hive_obj.split(".")[1]
        self.hive_col = hive_obj.split(".")[2]
        self.ora_sch = ora_obj.split(".")[0]
        self.ora_tbl = ora_obj.split(".")[1]
        self.ora_col = ora_obj.split(".")[2]


    def make_stmt(self, fun):
        if self.hive_col != "__ALL__":
            return fun()
        else:
            pass

    @orasql("1")
    def fn_ora_sum(self):
        return "SUM({0}) AS SUM_{0}".format(self.ora_col)

    @hiveql("1")
    def fn_hive_sum(self):
        return "SUM({0}) AS SUM_{0}".format(self.hive_col)

    @orasql("1")
    def fn_ora_avg(self):
        return "AVG({0}) AS AVG_{0}".format(self.ora_col)

    @hiveql("1")
    def fn_hive_avg(self):
        return "AVG({0}) AS AVG_{0}".format(self.hive_col)

    @orasql("1")
    def fn_ora_count(self):
        return "COUNT(1) AS CNT_{0}".format(self.ora_col)

    @hiveql("1")
    def fn_hive_count(self):
        return "COUNT(1) AS CNT_{0}".format(self.hive_col)

    @orasql("IS_NULL")
    def fn_ora_isnull(self):
        return "COUNT(1) AS NULLCNT_{0}".format(self.ora_col)

    @hiveql("IS_NULL")
    def fn_hive_isnull(self):
        return "COUNT(1) AS NULLCNT_{0}".format(self.hive_col)

    @orasql("1")
    def fn_ora_dcount(self):
        return "COUNT(DISTINCT {0}) AS DCNT_{0}".format(self.ora_col)

    @hiveql("1")
    def fn_hive_dcount(self):
        return "COUNT(DISTINCT {0}) AS DCNT_{0}".format(self.hive_col)

    @orasql("1")
    def fn_ora_star(self):
        return "*"

    @hiveql("1")
    def fn_hive_star(self):
        return "*"

    @oragrp("1")
    def fn_ora_group(self):
        return "{0}, COUNT(1)".format(self.ora_col)

    @hivegrp("1")
    def fn_hive_group(self):
        return "{0}, COUNT(1)".format(self.hive_col)



