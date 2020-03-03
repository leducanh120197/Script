import os

url = r"\\server10\NIPA\2.Tranning\Training"

list_folders = os.listdir(url)
# print(list_folders)
with open("get_folder_names_result.txt", "w", encoding="utf-8") as rf:
    for item in list_folders:
        rf.write("%s\n" % item)
