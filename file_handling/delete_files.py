import os
def remove_file(f):
    if os.path.isfile(f):
        try:
            os.remove(f)
        except OSError as e:
            print(f"Error: {f} : {e.strerror}")
    else:
        print(f"Error: {f} not a valid file")

remove_file('./files/text.txt')