import os
import shutil

url = r""
list_style = open("list_style.txt").read().splitlines()

for dirs, folders, files in os.walk(url):
    for file in files:
        if not file.endswith(".png"):
            continue
        for line in list_style:
            if file.__contains__(line):
                destination = os.path.join(dirs, "-template_"+line)
                os.makedirs(destination, exist_ok=True)
                shutil.move(os.path.join(dirs, file), destination)
                break
