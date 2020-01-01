import xml.dom.minidom
import os
import csv
import shutil
import codecs
import re
import datetime

url = r""
att = r"sample_attribute.csv"
rs = codecs.open("Eng_result.txt", "+w", encoding="utf-8")

print(datetime.datetime.now())

def change(var):
    if str(var).__contains__("."):
        num = int(int(var[:-(len(var)-var.rfind("."))])/48)
    else:
        num = int(int(var)/48)
    return num

def change_label(var):
    new_var = str(var).lower().strip().replace("\n", "")
    rs = re.sub("[^A-Za-z ]", "", new_var)
    return rs


for dirs, folders, files in os.walk(url):
    for file in files:
        if file.endswith("antx"):
            fileNum = file.rstrip(".antx")
            new_path = os.path.join(dirs, fileNum + "_seg.csv")
            # att_path = os.path.join(dirs, fileNum + "_attribute.csv")
            # shutil.copy(att, att_path)
            # os.remove(new_path)
            try:
                path = os.path.join(dirs, file)
                DOMTree = xml.dom.minidom.parse(path)
                collection = DOMTree.documentElement

                Segments = collection.getElementsByTagName("Segment")
                with open(new_path, "w", newline='') as csv_output:
                    writer = csv.writer(csv_output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(["CLASS","START_TIME","END_TIME","NOISE"])
                    for segment in Segments:
                        tmp = []
                        label = segment.getElementsByTagName("Label")[0].childNodes[0].data
                        new_label = change_label(label)
                        tmp.append(new_label)

                        start = segment.getElementsByTagName("Start")[0].childNodes[0].data
                        startNum = change(start)
                        tmp.append(startNum)

                        duration = segment.getElementsByTagName("Duration")[0].childNodes[0].data
                        durationNum = change(duration)
                        endNum = startNum + durationNum
                        tmp.append(endNum)
                        tmp.append("speech_clean")
                        writer.writerow(tmp)
                csv_output.close()
            except BaseException as BE:
                print(os.path.join(dirs, file) + "\\" + "{}".format(BE))

print(datetime.datetime.now())
