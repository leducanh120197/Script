import os
import shutil
import codecs

url= r"\\server10\NIPA\Voice_labeling\ANT"

destination = r"\\server10\NIPA\Voice_labeling\FINAL_RESULT\ant_error"

accepted_folders = open('list.txt', encoding="utf-8-sig").read().splitlines()

copied = []

for dirs1, folders1, files1 in os.walk(destination):
    for file1 in files1:
        copied.append(file1)
# print(copied)

for dirs, folders, files in os.walk(url):
    for file in files:
        if file in accepted_folders:
            path = os.path.join(dirs, file)
            if file not in copied:
                try:
                    shutil.copy(path, destination)
                    copied.append(file)
                except BaseException as BE:
                    print(dirs + file + "{}".format(BE))
            else:
                print(path + " : " + file)
