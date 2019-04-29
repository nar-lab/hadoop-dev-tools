#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from engine.log_extractor import LogExtractor

def main():
    """
    **** Usage: python log_extracttor_main.py [LOGFILENAME]
        + Parameter file: fs.resource/logparser-settings.txt

    **** Logfile settings (JSON):
        + logLevel: [INFO, DEBUG, WARN, ERROR]
        + logType:
            - sqoop second parameters, beeline default BEE
        + searchPattern: search regex pattern
        + extractPattern: extract regex pattern

    """
    if len(sys.argv) == 1:
        print(main.__doc__)
    else:
        l = LogExtractor(sys.argv[1])
        print(l.extract_logs())


if __name__ == "__main__":
    main()
