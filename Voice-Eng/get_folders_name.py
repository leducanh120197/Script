import os

url = r"\\server10\NIPA\Voice_Eng\Final_result\Dec-18"

list_folders = os.listdir(url)
print(list_folders)
# print(list_folders)
with open("get_folder_names_result.txt", "w", encoding="utf-8") as rf:
    for item in list_folders:
        rf.write(item + "\n")
