import os
import shutil
import codecs

url= r"\\server10\NIPA\Voice_Eng\Final_result\Phase_01_02"

destination = r"\\server10\NIPA\Voice_Eng\Rework\Phase_02"

accepted_folders = open('copy_files_input.txt', encoding="utf-8-sig").read().splitlines()

copied = []

for dirs1, folders1, files1 in os.walk(destination):
    for file1 in files1:
        copied.append(file1)
# print(copied)

for dirs, folders, files in os.walk(url):
    for file in files:
        if file.endswith("antx"):
            if file[:-(len(file)-file.rfind("."))] in accepted_folders:
                path = os.path.join(dirs, file)
                if file not in copied:
                    try:
                        shutil.copy(path, destination)
                        copied.append(file)
                    except BaseException as BE:
                        print(dirs + file + "{}".format(BE))
                else:
                    print(path + " : " + file)
