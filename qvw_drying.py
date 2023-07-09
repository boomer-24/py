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

# def copytreee(src, dst):
#     shutil.copytree(src, dst)

def LocalCopyAndDryingFile(localPathFrom, localPathTo):
    drying_command='"C:/Program Files/QlikView/Qv.exe" /r /visDrying=1 '
    shutil.copyfile(localPathFrom, localPathTo)
    command = drying_command + "'" + localPathTo + "'"
    os.system(command)

def TraverseDir(dirPathFrom, dirPathTo):
    for dr in os.listdir(dirPathFrom):
        abs_pathFrom = os.path.join(dirPathFrom, dr)
        abs_pathTo = os.path.join(dirPathTo, dr)

        if os.path.isdir(abs_pathFrom):
            TraverseDir(abs_pathFrom, abs_pathTo)
        elif dr.endswith('.qvw'):
            LocalCopyAndDryingFile(abs_pathFrom, abs_pathTo)

dirLocalSrc = "E:\QVProjects — копия"
dirLocalDst = "E:\QVProjects — копия2 " + str(date.today())

TraverseDir(dirLocalSrc, dirLocalDst)

            # qvwFilesLocalFrom.append(abs_pathFrom)
            # qvwFileLocalTo = os.path.join(localDst, dr)
            # qvwFilesLocalTo.append(qvwFileLocalTo)

# copytreee(src, dst)

# qvwFilesLocalFrom=[]
# qvwFilesLocalTo=[]
# drying_command='"C:/Program Files/QlikView/Qv.exe" /r ' #РАБОТАЕТ
# drying_command='"C:/Program Files/QlikView/Qv.exe" /r /visDrying=1 ' #РАБОТАЕТ
# drying_command='"C:/Program Files/QlikView/Qv.exe" /r /visDrying=1 '

# for filePath in qvwFilesLocalFrom:
#     print(filePath)
#     LocalCopyAndDryingFile(filePath, localPathTo, drying_command)


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