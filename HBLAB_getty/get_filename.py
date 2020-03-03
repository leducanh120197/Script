import os
import codecs

rs = codecs.open("get_filename_rs.txt", "+w", encoding="utf-8")
url = r"\\server10\Hblab\1. Customer\1.Video\part_01_50video"

for dirs, folders, files in os.walk(url):
    for file in files:
        if file.endswith(".mov"):
            rs.write(dirs + "\\" + file + "\n")