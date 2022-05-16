import os
def get_files(path):
    FileNames = []
    for filepath,dirnames,filenames in os.walk(path):
        FileNames = filenames
    return FileNames