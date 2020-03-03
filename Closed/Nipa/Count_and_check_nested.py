import os
import codecs

# url = r"\\server10\NIPA\2.Tranning\Training\24_Oct"
url = r"C:\Users\leduc\Desktop\output"

ft = codecs.open("count_result.txt", "w", "utf-8")
nested = codecs.open("count_result.txt", "w", "utf-8")
nested_list = []
for dir, folders, files in os.walk(url):
    for folder in folders:
        if folder.startswith("2019") and folder.count("_") == 5:
            path = os.path.join(dir, folder)
            for dirpath, fs, filenames in os.walk(path):
                countImage = 0
                countJson = 0
                for filename in filenames:
                    if filename.endswith(".jpg"):
                        countImage -= -1
                    if filename.endswith(".json"):
                        countJson -= -1
                # print(folder + " : " + str(countImage) + " : " + str(countJson) + "\n")
                ft.write(folder + " : " + str(countImage) + " : " + str(countJson) + "\n")
                for f in fs:
                    # nested.write(path + "\n")
                    nested_list.append(path)
print(nested_list)
