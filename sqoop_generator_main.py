#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from engine.sqoop_generator import SqoopGenerator
import pprint

def main():
    """
    **** Usage: python sqoop_generator_main.py [SCHEMA_NAME].[TABLE_NAME]
        + Parameter file: fs.resource/generator-settings.txt
        + Parameter file pattern: JOB:[SCH].[TBL];[KEY]:[VAL]

    **** Parameter file options:
        + JOB:[SCH].[TBL] > Db Object Name
        + TEMPLATE: [BASIC_IMP_CMD], [BASIC_IMP_OPT], [SPLIT_IMP_CMD], [SPLIT_IMP_OPT], [DIRECT_IMP_CMD], [DIRECT_IMP_OPT], [BASIC_EXP_CMD], [BASIC_EXP_OPT]
            - BASIC_IMP_CMD: import command with default settings (default)
            - BASIC_IMP_OPT: import option file with default settings except initialize parameteres
            - BASIC_IMP_OPT_INIT: import option file with default settings with initialize parameteres
            - SPLIT_IMP_CMD: import command with split by and multi mappers
            - SPLIT_IMP_OPT: import option file with split by and multi mappers except initialize parameteres
            - SPLIT_IMP_OPT_INIT: import option file with split by and multi mappers with initialize parameteres
            - DIRECT_IMP_CMD: import command with direct and multi mappers
            - DIRECT_IMP_OPT: import option file with direct and multi mappers except initialize parameteres
            - DIRECT_IMP_OPT_INIT: import option file with direct and multi mappers with initialize parameteres
            - BASIC_EXP_CMD: export command with default settings
            - BASIC_EXP_OPT: export option file with default settings except initialize parameteres
        + HDFS: Hdfs target path
        + FETCHSIZE: sqoop fetch size option (default: 1000)
        + SPLITCOL: can be used with SPLIT_IMP_* templates, sqoop split-by option
        + NMAP: can be used with SPLIT_IMP_* templates, -m, --num-mappers option, (default: 20)

    *** For init file: python sqoop_generator_main.py __INIT__

    """
    if len(sys.argv) == 1:
      print(main.__doc__)
    else:
        s = SqoopGenerator(sys.argv[1])
        print(s.generate())


if __name__ == "__main__":
    main()



