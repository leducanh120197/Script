import os
import shutil

url = r"\\server10\NIPA\Voice_Eng\Phase_02"
dst = r"\\server10\NIPA\Voice_Eng\backup_csv_01_02\antx\phase_02"
# file_move = open(r"move_file_input.txt").read().splitlines()

for dirs, folders, files in os.walk(url):
    for file in files:
        if file.endswith(".antx"):
            try:
                # print(file)
                new_url = os.path.join(dirs, file)
                new_dst = os.path.join(dst, file)
                shutil.move(new_url, new_dst)
            except BaseException as BE:
                print(file + "\\" + BE)