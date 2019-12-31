import os
import codecs

url = r"\\server10\NIPA\Voice_Eng\Delivered"
rs = codecs.open("result.txt", "+w", encoding="utf-8")

for dirs, folders, files in os.walk(url):
    for folder in folders:
        if folder.startswith("Folder_"):
            rs.write(dirs + "\\" + folder + "\n")