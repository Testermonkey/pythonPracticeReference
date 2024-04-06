import zipfile

to_zip = ['./files/subfolder/01_file_test.csv', 
    './files/subfolder/01_file_test.txt', 
    './files/subfolder/01_test_file.csv', 
    './files/subfolder/01_test_file.txt',
    './files/01_file_test.csv',
    './files/01_file_test.txt']

def create_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive:
        for f in files:
            archive.write(f)

def add_to_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt) as archive:
        for f in files:
            lst = archive.namelist()
            if not f in lst:
                archive.write(f)
            else:
                print(f'File exist in Zip {f}')

def read_zip(zipf):
    with zipfile.ZipFile(zipf, 'r') as archive:
        lst = archive.namelist()
        for l in lst:
            zfinf = archive.getinfo(l)
            print(f'{l} => {zfinf.file_size} bytes, {zfinf.compress_size} compressed')

def extract_file(zipf, fn, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extract(fn, path=path)

def extract_all(zipf, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extractall(path=path)


# create_zip('./files.zip', to_zip, 'w')
# add_to_zip('./files.zip', to_zip, 'a')
# read_zip('./files.zip')
extract_file('./files.zip', 'files/01_file_test.txt', 'extracted')