import os
import codecs

url = r"\\172.16.8.10\Noul_Medical\Output_IMG_collection\Annotation_IMG\Output"



rs = codecs.open("count_text_result.txt", "w", "utf-8")
for dir, folders, files in os.walk(url):
    for folder in folders:
        if folder.__contains__("-"):
            if folder.__contains__("_"):
                txt = 0
                path = os.path.join(dir, folder)
                for dirpath, f, filenames in os.walk(path):
                    for filename in filenames:
                        if filename.endswith(".txt"):
                            txt += 1
                rs.write(folder + " : " + str(txt)+ "\n")
    