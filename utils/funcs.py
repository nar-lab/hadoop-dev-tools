#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 13:16:36 2018

@author: Ali Cabukel
"""

class Funcs(object):

    def __init__(self):
        pass

    def map_generator_object(self, object_list, obj_sep, obj_name):
        return [(v.split(":")) for k,v in object_list if k.split(obj_sep) == ["JOB",obj_name]]

    def fn_dict_formatter(self, object_list):
        return ";".join([k + ":" + v for k, v in object_list])

    def fn_object_formatter(self, sch, tbl, col):
        return "{0}.{1}.{2}".format(sch, tbl, col)

    def map_validation_object(self, object_list, header):
        map_object_list = []
        for o in object_list:
            validation_map = dict()
            for i in range(len(o)):
                validation_map[header[i]] = o[i]
            map_object_list.append(validation_map)
        return map_object_list

    def loglines2dict_bee(self,log_lines):
        return {"log_level":log_lines[0].strip(),
                "log_type": "BEE",
                "log_details": log_lines[1:]
                }

    def loglines2dict_sqoop(self, log_lines):
        return {"log_level": log_lines[0].split(" ")[2],
                "log_type": log_lines[0].split(" ")[3],
                "log_details": log_lines[1:]
                }

    def loglines2dict_hive(self, log_lines):
        return {"log_level": log_lines[1].split(" ")[0],
                "log_type": log_lines[1].split(" ")[1],
                "log_details": log_lines[1:]
                }
                
    def get_generator_value(self, obj_data, key):
        if obj_data:
            return [x[1] for x in obj_data if x[0] == key]
        return None