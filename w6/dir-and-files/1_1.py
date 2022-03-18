import os
from fnmatch import fnmatch

root = 'c:\\Users\\orazg\\OneDrive\\Рабочий стол\\pp2_2022_spring'
pattern = "*.*"

for path, subdirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, pattern):
            print(os.path.join(path, name))