import os
import shutil
import codecs

url = r""
destination = r""


rs = codecs.open("copy_folders_error.txt", "+w", encoding="utf-8")
accepted_folders = open('copy_folders_input.txt', encoding="utf-8-sig").read().splitlines()
totalFolder = len(accepted_folders)
c = 0
copied = []

for dirs, folders, files in os.walk(url):
    dir_base = os.path.basename(dirs)
    if dir_base not in accepted_folders:
        continue
    else:
        try:
            print(dir_base)
            shutil.copytree(dirs, os.path.join(destination, dir_base))
            c += 1
            print(dirs + " Done " + str(c) + "/" + str(totalFolder))
            copied.append(dir_base)
        except BaseException as BE:
            print(dirs + "{}".format(BE))
            rs.write(dirs + "{}".format(BE))

for item in accepted_folders:
    if item not in copied:
        rs.write("%s\n" % item + "can't copy")

