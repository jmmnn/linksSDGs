'# -*- coding: utf-8 -*-'

import subprocess

# import sys
# import csv
# import os
# import glob

result = []
def concatFiles():
    for filename in glob.glob(os.path.join('names/', '*.txt')):
        # do your stuff
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            #keep only 4 letter names, not ending with "i" or "y"
            for row in reader:
                if row[1] == 'F' and 3 < len(row[0]) < 5 and not(row[0].endswith('i')) and not(row[0].endswith('y')):
                    result.append(row[0])
    return result

#execute concatenation
concatFiles()

subprocess.call("test1.py", shell=True)