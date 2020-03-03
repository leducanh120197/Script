import xml.dom.minidom
import os
import csv
import shutil
import codecs
import re
import datetime

url = r"\\server10\NIPA\Voice_Eng\Final_result\Phase_01_02"
rs = codecs.open("Eng_result.txt", "+w", encoding="utf-8")

for dirs, folders, files in os.walk(url):
    for file in files:
        if file.endswith("antx"):
            try:
                path = os.path.join(dirs, file)
                DOMTree = xml.dom.minidom.parse(path)
                collection = DOMTree.documentElement

                Configuration = collection.getElementsByTagName("Configuration")
                for segment in Configuration:
                    key = segment.getElementsByTagName("Key")[0].childNodes[0].data
                    if key == "Samplerate":
                        var = segment.getElementsByTagName("Value")[0].childNodes[0].data
                        if var != "48000":
                            rs.write(file + "      " + var +"\n")
            except BaseException as BE:
                print(os.path.join(dirs, file) + "\\" + "{}".format(BE))