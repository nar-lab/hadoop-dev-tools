#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from engine.sql_generator import ValidationParser

def main():
    """
    **** Usage: python data_validator_main.py [OBJ]

    """
    if len(sys.argv) == 1:
        print(main.__doc__)
    else:
        v = ValidationParser()
        args = dict()
        print(v.find_validation_object(HIVE_SCH="BERKA_DB",
                                       HIVE_TBL="BERKA_TBL",
                                       HIVE_COL="BERKA_COL",
                                       ORA_SCH="DB_BERKA_DB",
                                       ORA_TBL="DB_BERKA_TBL",
                                       ORA_COL="DB_BERKA_COL"))


if __name__ == "__main__":
    main()
