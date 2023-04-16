# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# test_list_tour = [1, 2, 3, 4, 5]

# test_dict_tour = {'a': 1, 'b': 2}

# print(test_dict_tour)

# print(test_list_tour)


# print(test_dict_tour.get('b'))

# import os
# print(os.getcwd())



# import os
# import shutil

# print('BEFORE:', os.listdir('E:/'))
# shutil.copyfile('E:/QVProjects — копия/1.qvw', 'E:/QVProjects — копия2/1.qvw')
# print('AFTER:', os.listdir('E:/'))







import os
from datetime import date
import shutil

def copytreee(src, dst):
    shutil.copytree(src, dst)

qvwfiles=[]
# drying_command='"C:/Program Files/QlikView/Qv.exe" /r ' #РАБОТАЕТ
# drying_command='"C:/Program Files/QlikView/Qv.exe" /r /visDrying=1 ' #РАБОТАЕТ
drying_command='"C:/Program Files/QlikView/Qv.exe" /r /visDrying=1 '

def TraverseDir(cur):
    print('    TraverseDir ' + cur)

    for dr in os.listdir(cur):
        abs_path = os.path.join(cur, dr)
        # print('  TraverseDir abs_path: ' + abs_path)

        if os.path.isdir(abs_path):
            # print('dir')
            TraverseDir(abs_path)
#.qvw мб в имени папки!
        # elif 'qvw' in dr[-3:]:
        elif dr.endswith('.qvw'):
            # qvwfiles.append(abs_path)
            comm = drying_command
            comm += ("'")
            comm += (abs_path)
            comm + ("'")
            qvwfiles.append(comm)
            # print(abs_path)

src = "E:\QVProjects — копия"
dst = "E:\QVProjects — копия2 " + str(date.today())

copytreee(src, dst)

TraverseDir(dst)

for command in qvwfiles:
    print(command)
    os.system(command)



# drying_command='"C:/Program Files/QlikView/Qv.exe" /r '
# for file in qvwfiles:
#     drying_command += file

# # os.system('"C:/Program Files/QlikView/qv.exe" /r /visDrying=1  "E:/QVProjects — копия/1.qvw"')
# drying_command='"C:/Program Files/QlikView/Qv.exe" /r /visDrying=1 '
# drying_command='"C:/Program Files/QlikView/Qv.exe" /r '
# drying_command +="'E:/QVProjects — копия/1.qvw'"

# print (drying_command)
# os.system(drying_command)



# mas = os.listdir('E:/QVProjects — копия')
# qvwmas = [os.path.abspath(os.path.dirname(file)) for file in mas if file.endswith("qvw")]

# # filename = os.path.join(basedir, 'test.txt')
# print(mas)
# print(qvwmas)