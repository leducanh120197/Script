import os
import codecs

url = r"\\server10\NIPA\Voice_labeling\Feedback"

rs = codecs.open("get_folders_result.txt", "+w", encoding="utf-8")

for dirs, folders, files in os.walk(url):
    for folder in folders:
        if folder.startswith("label") or folder.startswith("noise") :
            path = os.path.join(dirs, folder)
            for dir2, folder2, file2 in os.walk(path):
                for fd in folder2:
                    rs.write(dir2 + "\\" + fd + "\n")

# scan 1 tầng
# list_folders = os.listdir(url)
# with open("get_folder_names_result.txt", "w", encoding="utf-8") as rf:
#     for item in list_folders:
#         rf.write(item + "\n")