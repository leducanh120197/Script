import os
import codecs

rs = codecs.open("get_filename_rs.txt", "+w", encoding="utf-8")
url = r"\\server10\NIPA\Sotatek\02282020\Cabbage\Target_image-20200228T033019Z-001\Target_image"

for dirs, folders, files in os.walk(url):
    for file in files:
        if file.endswith("json"):
            continue
        if file.endswith("db"):
            continue
        rs.write(dirs + "\\" + file + "\n")