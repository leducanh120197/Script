import os
import shutil

url = r""

for dirs, folders, files in os.walk(url):
    for folder in folders:
        if folder.startswith("-template_"):
            dirpath = os.path.join(dirs, folder)
            for d, fs, fl in os.walk(dirpath):
                list_img = []
                list_txt = []
                for file in fl:
                    if file.endswith(".png"):
                        list_img.append(os.path.splitext(file)[0])
                    elif file.endswith(".txt"):
                        source_file = os.path.join(d, file)
                        list_txt.append(os.path.splitext(file)[0])
                if not list_txt:
                    continue
                for list in list_img:
                    if list not in list_txt:
                        shutil.copy(source_file, os.path.join(d, list+".txt"))
