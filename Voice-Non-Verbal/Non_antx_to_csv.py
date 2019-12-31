from xml.dom.minidom import parse
import xml.dom.minidom
import os
import csv

url = r"\\server10\NIPA\Voice_labeling\Dec-24"
# url = r"\\server10\NIPA\Voice_labeling\Source\Source\아기울음소리"

baby_error = open(r".\error list\baby_cry.txt").read().splitlines()
bark_error = open(r".\error list\bark.txt").read().splitlines()
horn_error = open(r".\error list\horn.txt").read().splitlines()
clap_error = open(r".\error list\clap.txt").read().splitlines()
cough_error = open(r".\error list\cough.txt").read().splitlines()
gun_error = open(r".\error list\gun.txt").read().splitlines()
scream_error = open(r".\error list\scream.txt").read().splitlines()
siren_error = open(r".\error list\siren.txt").read().splitlines()
speech_error = open(r".\error list\speech.txt").read().splitlines()
noise_error = open(r".\error list\noise.txt").read().splitlines()


def change(var):
    if str(var).__contains__("."):
        num = int(int(var[:-(len(var)-var.rfind("."))])/48)
    else:
        num = int(int(var)/48)
    return num


def segment_error(varx):
    var = str(varx).strip().replace("\n","")
    if var in baby_error:
        var = "baby_cry"
    elif var in bark_error:
        var = "bark"
    elif var in clap_error:
        var = "clap"
    elif var in cough_error:
        var = "cough"
    elif var in gun_error:
        var = "gun"
    elif var in horn_error:
        var = "horn"
    elif var in scream_error:
        var = "scream"
    elif var in siren_error:
        var = "siren"
    elif var in speech_error:
        var = "speech"
    return var


for dirs, folders, files in os.walk(url):
    for file in files:

        list1 = []
        if file.endswith("antx"):
            new_path = os.path.join(dirs, file.rstrip(".antx") + ".csv")
            os.remove(new_path)
            # read antx
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
                        new_label = segment_error(label)
                        tmp.append(new_label)

                        start = segment.getElementsByTagName("Start")[0].childNodes[0].data
                        startNum = change(start)
                        tmp.append(startNum)

                        duration = segment.getElementsByTagName("Duration")[0].childNodes[0].data
                        durationNum = change(duration)
                        endNum = startNum + durationNum
                        tmp.append(endNum)

                        parameter = segment.getElementsByTagName("Parameter1")[0].childNodes[0].data
                        # if parameter in noise_error:
                        #     parameter = "1"
                        tmp.append(parameter)
                        list1.append(tmp)
                    for item in list1:
                        writer.writerow(item)
                csv_output.close()
            except BaseException as BE:
                print(file + "\\" + "{}".format(BE))
