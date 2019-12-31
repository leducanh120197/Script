import xml.dom.minidom
import os
import codecs
import re
import datetime

# url = r"C:\Users\LQA\OneDrive\Máy tính\New folder\Folder_72"
url = r"\\server10\NIPA\Voice_Eng\Phase_01"
rs = codecs.open("check_txt.result.txt", "+w", encoding="utf-8")

except_list = []

print(datetime.datetime.now())


def change_label(var):
    new_var = str(var).lower().strip()
    new_var = rm_escape(new_var)
    rs = re.sub("[^A-Za-z ]", "", new_var)
    return rs


def rm_escape(var):
    var = str(var).replace("\n","").replace("\t", "")
    return var


for dirs, folders, files in os.walk(url):
    for file in files:
        if file.endswith("antx"):
            fileNum = file.rstrip(".antx")
            try:
                text = list(open(os.path.join(dirs, fileNum + ".txt"), "r", encoding="utf-8").read().split(" "))
                segmenttxt = []
                path = os.path.join(dirs, file)
                DOMTree = xml.dom.minidom.parse(path)
                collection = DOMTree.documentElement

                Segments = collection.getElementsByTagName("Segment")
                for segment in Segments:
                    label = segment.getElementsByTagName("Label")[0].childNodes[0].data
                    new_label = change_label(label)
                    segmenttxt.append(new_label)

                x = str(set(segmenttxt) - set(text))
                y = str(set(text) - set(segmenttxt))
                if x != "set()" or y != "set()":
                    rs.write(dirs + "\\" + fileNum + "\\" + x + "\\" + y + "\\" + str(text) + "\n")
            except BaseException as BE:
                x = path + "\\" + "{}".format(BE)
                except_list.append(x)
for i in except_list:
    rs.write(i + "\n")

print(datetime.datetime.now())
