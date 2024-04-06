import shutil

def move_files(src, dest):
    shutil.move(src, dest)

move_files('./files/test.txt', './files/subfolder/text.txt')