import os
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
# первый скрипт
# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     dir_name = 'dir_' + str(i)
#     os.makedirs(dir_name)
# второй скрипт
# for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     dir_name = 'dir_' + str(i)
#     os.removedirs(dir_name)
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# allindir = os.listdir()
# onlydir =[]
# for i in allindir:
#     if os.path.isdir(i) is True:
#         onlydir.append(i)
# print(onlydir)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
print (os.path.basename(__file__))
shutil.copyfile(os.path.basename(__file__), 'copy.py')