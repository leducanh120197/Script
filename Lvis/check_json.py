import json
import os
import codecs

json1 = []

rs = codecs.open("check_json_rs.txt", "+w", encoding="utf-8")
url = r"\\server10\NIPA\Lvis_Project\Output"
for dirs, folders, files in os.walk(url):
    for file in files:
        if file.endswith("json"):
            with open(os.path.join(dirs, file), encoding="utf-8") as json_file:
                data = json.load(json_file)
                try:
                    for p in data["images"]:
                        rs.write(dirs + "\\" + file + "\\" + p["file_name"] + "\n")
                except:
                    print(dirs + file)
            # rs.write("------------------------------------------------------" + "\n")