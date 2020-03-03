import os
import codecs

url = r"\\server10\NIPA\2.Tranning\Training\23_Oct"
# url = r"C:\Users\leduc\Desktop\23"

list_current = os.listdir(url)

ft = codecs.open("count_current_result.txt", "w", "utf-8")

for f in list_current:
    path = os.path.join(url, f)
    countImages = 0
    countJson = 0
    for dir, folders, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith(".jpg"):
                countImages -= -1
            if filename.endswith("json"):
                countJson -= -1
    ft.write(f + " : " + str(countImages) + " : " + str(countJson)+ "\n")
