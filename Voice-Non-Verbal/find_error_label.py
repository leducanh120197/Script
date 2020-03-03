from xml.dom.minidom import parse
import xml.dom.minidom
import os
import codecs

url = r"\\server10\NIPA\Voice_labeling\__Feb21"

rs = codecs.open("find_error_result.txt", "w", "utf-8")

label_list = ["bark", "siren", "horn", "clap", "cough", "speech", "baby_cry", "scream", "gun"]
noise_list = ["0", "1", "2", "3"]

def change_label(varx):
    var = str(varx).strip().replace("\n", "")
    return var

for dirs, folders, files in os.walk(url):
    for file in files:
        if file.endswith("antx"):
            try:
                path = os.path.join(dirs, file)
                DOMTree = xml.dom.minidom.parse(path)
                collection = DOMTree.documentElement

                #get Segment
                Segments = collection.getElementsByTagName("Segment")
                for segment in Segments:
                    tmp = []
                    label = segment.getElementsByTagName("Label")[0].childNodes[0].data
                    new_label = change_label(label)
                    if new_label not in label_list:
                        rs.write("LABEL" + "\\" + dirs + "\\" + file + "\\"+ label + "\n")

                    parameter = segment.getElementsByTagName("Parameter1")[0].childNodes[0].data
                    new_noise = change_label(parameter)
                    if new_noise not in noise_list:
                        rs.write("NOISE" + "\\" + dirs + "\\" + file + "\\"+ parameter + "\n")
            except BaseException as BE:
                print(file + "\\" + "{}".format(BE))
                rs.write("EXCEPT" + "\\" + dirs + "\\" + file + "\\" + "{}".format(BE) + "\n")
