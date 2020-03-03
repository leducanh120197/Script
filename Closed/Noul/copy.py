import os
import shutil

url = r""
destination = r""

accepted_folders = open('list.txt', encoding="utf-8-sig").read().splitlines()
n = len(accepted_folders)
c = 0
copied_folders = []
remaining_folder = []

# print(accepted_folders)

for dirpath, dirnames, filenames in os.walk(url):
    dirpath_base = os.path.basename(dirpath)
    # print(dirpath_base)
    if dirpath_base not in accepted_folders:
        continue
    else:
        c += 1
        print(dirpath_base)
        output = os.path.join(destination, dirpath_base)
        shutil.copytree(dirpath, output, ignore=shutil.ignore_patterns('*.db', "*.ini"))
        print(dirpath + " DONE " + str(c) + "/" + str(n))
        copied_folders.append(dirpath_base)
for fn in accepted_folders:
    if fn not in copied_folders:
        remaining_folder.append(fn)
with open("remaining_folders.txt", "w", encoding="utf-8") as rf:
    for item in remaining_folder:
        rf.write("%s\n" % item)
with open("copied_folders.txt", "w", encoding="utf-8") as rff:
    for i in copied_folders:
        rff.write("%s\n" % i)
