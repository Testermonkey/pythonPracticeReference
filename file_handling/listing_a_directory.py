import os

def list_dir(folder):
    for fn in os.listdir(folder):
        print(fn)

list_dir('./files')