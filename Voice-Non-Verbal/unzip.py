import zipfile
import os
import datetime
import shutil

url = r"C:\Users\LQA\OneDrive\Máy tính\New folder"
# url = r"\\server10\NIPA\Voice_Eng\Dec-25"
dst = r"\\server10\Voice\Tool and Samples\ant_backup"
# url = r"C:\Users\LQA\OneDrive\Máy tính\x"
# dst = r"C:\Users\LQA\OneDrive\Máy tính\y"

print("ant => antx: Doing" + datetime.datetime.now())
for dirs, folders, files in os.walk(url):
    for file in files:
         if file.endswith(".ant"):
            try:
                with zipfile.ZipFile(os.path.join(dirs,file)) as Zip:
                    for Zip_info in Zip.infolist():
                        if Zip_info.filename[-1] == '/':
                            continue
                        Zip_info.filename = file + "x"
                        Zip.extract(Zip_info, dirs)
                shutil.move(os.path.join(dirs,file), os.path.join(dst,file))
            except BaseException as BE:
                print(dirs + "\t" + file + "\t" + "{}".format(BE))
print("ant => antx: Done" + datetime.datetime.now())
