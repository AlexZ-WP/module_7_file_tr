import os
from datetime import datetime

directory = '/Users/Alex/Documents/PycharmProjects/pythonProject/module_7'


file = [f for f in os.listdir(directory) if os.path.isfile(f)]
print(file)
dir_ = [d for d in os.listdir() if os.path.isdir(d)]
print(dir_)

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath) # указывается полный путь filepath
        formatted_ftime = datetime.fromtimestamp(filetime)
        filesize = os.stat(filepath).st_size
        parent_dir = root

    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_ftime},'
            f' Родительская директория: {parent_dir}')

print(root, dirs, files)
print(filepath)