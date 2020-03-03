import os
import codecs

url = r"\\server10\NIPA\Fighting\Tool&guide\fightAnnotation\annotationOnly"
rs = codecs.open("count_folder_result.txt", "+w", encoding="utf-8")

for dirs, folders, files in os.walk(url):
    for folder in folders:
        if folder.count("_")==2:
            path = os.path.join(dirs, folder)




