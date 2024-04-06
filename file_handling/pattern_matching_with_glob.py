from pathlib import Path

def glob_match(folder, search):
    p = Path(folder)
    for n in p.glob(search):
        print(n)

#glob_match('./files', '*2*.t*')
glob_match('./files/subfolder', '*_file_*.t*')