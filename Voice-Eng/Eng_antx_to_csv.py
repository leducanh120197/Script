import xml.dom.minidom
import os
import csv
import shutil
import codecs
import re
import datetime

# url = r"\\server10\NIPA\Voice_Eng\Phase_03\Feb-12"
url = r"C:\Users\LQA\OneDrive\Máy tính\xxx"
# url = r"C:\Users\LQA\OneDrive\Máy tính\New folder"
rs = codecs.open("Eng_result.txt", "+w", encoding="utf-8")

print(datetime.datetime.now())

def change(var, config_samplerate):
    new_samplerate = int(config_samplerate)/1000
    if str(var).__contains__("."):
        num = int(int(var[:-(len(var)-var.rfind("."))])/new_samplerate)
    else:
        num = int(int(var)/new_samplerate)
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

                # get Samplerate
                Configuration = collection.getElementsByTagName("Configuration")
                for config in Configuration:
                    key = config.getElementsByTagName("Key")[0].childNodes[0].data
                    if key == "Samplerate":
                        config_samplerate = config.getElementsByTagName("Value")[0].childNodes[0].data


                list_segment = []
                #get Segment
                Segments = collection.getElementsByTagName("Segment")
                with open(new_path, "w", newline='') as csv_output:
                    writer = csv.writer(csv_output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(["CLASS","START_TIME","END_TIME","NOISE"])
                    for segment in Segments:
                        tmp = []
                        label = segment.getElementsByTagName("Label")[0].childNodes[0].data
                        new_label = change_label(label)
                        tmp.append(new_label)
                        list_segment.append(label)

                        start = segment.getElementsByTagName("Start")[0].childNodes[0].data
                        startNum = change(start, config_samplerate)
                        tmp.append(startNum)

                        duration = segment.getElementsByTagName("Duration")[0].childNodes[0].data
                        durationNum = change(duration, config_samplerate)
                        endNum = startNum + durationNum
                        tmp.append(endNum)
 
                        tmp.append("speech_clean")
                        writer.writerow(tmp)
                    txtSegment_oneline = ''.join(list_segment).replace(" ", "")
                csv_output.close()

                text_oneline = open(os.path.join(dirs, fileNum + ".txt"), "r", encoding="utf-8").read().lower().replace("\n","").replace(" ", "")

                #create attribute.csv
                att_path = os.path.join(dirs, fileNum + "_attribute.csv")
                if text_oneline == txtSegment_oneline:
                    att = r"C:\Users\LQA\OneDrive\Máy tính\Script\Voice-Eng\sample_attribute_true.csv"
                    shutil.copy(att, att_path)
                else:
                    att = r"C:\Users\LQA\OneDrive\Máy tính\Script\Voice-Eng\sample_attribute_false.csv"
                    shutil.copy(att, att_path)
            except BaseException as BE:
                print(os.path.join(dirs, file) + "\\" + "{}".format(BE))

print(datetime.datetime.now())
