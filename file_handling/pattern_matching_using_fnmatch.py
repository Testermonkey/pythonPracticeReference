import os
import fnmatch


def match(folder, search):
    for fn in os.listdir(folder):
        if fnmatch.fnmatch(fn, search):
            print(fn)

match('./files', '*1*_file.csv')