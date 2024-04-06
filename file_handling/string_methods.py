import os

def ends_with(folder, search):
    for fn in os.listdir(folder):
        if fn.endswith(search):
            print(fn)

def starts_with(folder, search):
    for fn in os.listdir(folder):
        if fn.startswith(search):
            print(fn)

ends_with('./files', '.txt')
starts_with('./files', '01_test')