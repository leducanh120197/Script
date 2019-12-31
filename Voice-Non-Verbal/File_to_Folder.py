import os
import shutil

url = r"\\server10\NIPA\Voice_labeling\Source\Source\총소리"
folder_list = []

for dirs, folders, files in os.walk(url):
    for file in files:
        # if file.startswith("bark"):
        #     continue
        if file.endswith(".wav"):
            if dirs not in folder_list:
                folder_list.append(dirs)

for dir in folder_list:
    for d, fds, fls in os.walk(dir):
        folder_name = os.listdir(dir)[0][:-6]
        count = 0
        for fl in sorted(fls, key=len):
            if count == 0:
                num = 1
                dest = os.path.join(dir, folder_name + "_" + str(num))
                while os.path.exists(dest):
                    num += 1
                    dest = os.path.join(dir, folder_name + "_" + str(num))
                os.makedirs(dest)
                shutil.move(os.path.join(dir, fl), os.path.join(dest, fl))
                count += 1
            elif count == 99:
                shutil.move(os.path.join(dir, fl), os.path.join(dest, fl))
                count = 0
            else:
                shutil.move(os.path.join(dir, fl), os.path.join(dest, fl))
                count += 1
