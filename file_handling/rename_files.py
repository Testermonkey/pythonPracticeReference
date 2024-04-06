import os
from pathlib import Path

def rename1(src, dest):
    os.rename(src, dest)

def rename2(src, dest):
    f = Path(src)
    f.rename(dest)

    rename1('./files/text.txt', './files/test.txt')