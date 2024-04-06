import shutil

def copy_file(src, dest):
    shutil.copy(src, dest)

def copy_folder(src, dest):
    shutil.copytree(src, dest)

#copy_file('./files/02_file.txt', './files/subfolder' )
copy_folder('./files', './files/new_folder')