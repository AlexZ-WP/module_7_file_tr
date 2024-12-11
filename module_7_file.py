import os
from datetime import datetime
"""
Освоить работу с файловой системой в Python, используя модуль os.
Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize и использование 
модуля time для корректного отображения времени.
"""
directory = '/Users/Alex/Documents/PycharmProjects/pythonProject/module_7'
os.chdir('/Users/Alex/Documents/PycharmProjects/pythonProject/module_7')

file = [f for f in os.listdir(directory) if os.path.isfile(f)]
print(file)

dir_ = [d for d in os.listdir() if os.path.isdir(d)]
print(dir_)

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory, file)
        # filetime = os.path.getmtime(file)
        # formatted_ftime = datetime.fromtimestamp(filetime)
        # filesize = os.stat(file).st_size
        # parent_dir = directory

        print(file)
        print(filepath)