import os
import codecs

# url = r"\\server10\NIPA\Voice_Eng\Delivered"
url = r"\\server10\NIPA\Voice_labeling\Feedback\2nd"
rs = codecs.open("get_folders_result.txt", "+w", encoding="utf-8")

for dirs, folders, files in os.walk(url):
    for folder in folders:
        # if folder.startswith("rework_"):
        rs.write(dirs + "\\" + folder + "\n")

# scan 1 tầng
# list_folders = os.listdir(url)
# with open("get_folder_names_result.txt", "w", encoding="utf-8") as rf:
#     for item in list_folders:
#         rf.write(item + "\n")