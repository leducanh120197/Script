import os
import shutil
import codecs

# url = r"\\server10\Voice\Output"
# destination = r"D:\[Voice]Eng_Backup"

url = r"\\server10\Voice\Output"
destination = r"D:\[Voice]Eng_Backup\-Dec-25"

# url = r"\\server10\NIPA\Voice_Eng\Final_result\temple"
# destination = r"\\server10\NIPA\Voice_Eng\Final_result\templeantx"

# url = r"\\server10\NIPA\Voice_Eng\Part_1"
# destination = r"\\server10\NIPA\Voice_Eng\Delivered\Dec-13"

rs = codecs.open("move_folders_error.txt", "+w", encoding="utf-8")
accepted_folders = open('move_folders_input.txt', encoding="utf-8-sig").read().splitlines()
totalFolder = len(accepted_folders)
c = 0
moved = []

for folder in accepted_folders:
    try:
        # path = os.path.join(destination, folder)
        print(folder)
        shutil.move(os.path.join(url, folder), os.path.join(destination, folder))
        c += 1
        print(folder + " Done " + str(c) + "/" + str(totalFolder))
        moved.append(folder)
    except BaseException as BE:
        print(folder + "{}".format(BE))
        rs.write(folder + "{}".format(BE))

for item in accepted_folders:
    if item not in moved:
        rs.write("%s\n" % item + "can't move")
