import os

# url = r"\\172.16.8.10\Noul_Medical\Output_IMG_collection\Annotation_IMG\Output\Sep_05"

url = r"\\server10\NIPA\2.Tranning\Output\1025"

fr = open("check_fol_nested_result.txt", "w+", encoding="utf-8-sig")

for dirs, folders, files in os.walk(url):
    for folder in folders:
        if folder.startswith("2019") and folder.count("_") == 5:
                path = os.path.join(dirs, folder)
                for d, fs, fls in os.walk(path):
                    for f in fs:
                        fr.write(path + "\n")