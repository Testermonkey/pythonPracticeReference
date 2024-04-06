import os

def traverse(folder):
    for folder_path, dirs, files in os.walk(folder):
        print(f'Folder: {folder_path}')
        for fn in files:
            print(f'\t{fn}')


traverse('./files')