import os
import codecs
import csv

# url = r"\\server10\NIPA\Voice_Eng\Phase_03-DELIVERED"
# url_org = r"\\server10\NIPA\Voice_Eng\Phase_03\output-12"
url_org = r"\\server10\NIPA\Voice_Eng\Phase_02\part_02_5k"

matched = ["TRUE", "FALSE", "true", "false"]
tone = ["0", "1"]
sex = ["0", "1", "U", "u"]
speed = ["0", "1", "2"]
label = ["matched", "speaker_sex", "tone", "ATTRIBUTE", "speed"]
noise = ["NOISE", "speech_with_noise", "speech_clean"]


def check_att(url):
    a = "\\"

    rs = codecs.open("check_att_result.txt", "+w", encoding="utf-8")

    for dirs, folders, files in os.walk(url):
        for file in files:
            if file.__contains__("_attribute"):
                with open(os.path.join(dirs, file)) as csv_file:
                    try:
                        readCSV = list(csv.reader(csv_file, delimiter=","))
                        for row in readCSV:
                            if row[0] == "matched" and (str(row[1]).strip() not in matched):
                                rs.write("matched" + a + dirs + a + file + a + str(row[1]) + "\n")
                            if row[0] == "speaker_sex" and (str(row[1]).strip() not in sex):
                                rs.write("speaker_sex" + a + dirs + a + file + a + str(row[1]) + "\n")
                            if row[0] == "tone" and (str(row[1]).strip() not in tone):
                                rs.write("tone" + a + dirs + a + file + a + str(row[1]) + "\n")
                            if row[0] == "speed" and (str(row[1]).strip() not in speed):
                                rs.write("speed" + a + dirs + a + file + a + str(row[1]) + "\n")
                            if str(row[0]).strip() not in label:
                                rs.write("label" + a + dirs + a + file + a + str(row[0]) + "\n")
                    except BaseException as BE:
                        rs.write("EXCEPT" + a + os.path.join(dirs, file) + a + "{}".format(BE) + "\n")
                csv_file.close()
            if file.__contains__("_seg"):
                with open(os.path.join(dirs, file)) as csv_file:
                    try:
                        readCSV = list(csv.reader(csv_file, delimiter=","))
                        for row in readCSV:
                            if str(row[3]).strip() not in noise:
                                rs.write("noise" + a + dirs + a + file + a + str(row[3]) + "\n")
                    except BaseException as BE:
                        rs.write("EXCEPT" + a + os.path.join(dirs, file) + a + "{}".format(BE) + "\n")
                csv_file.close()


def check_de(url):
    rs = codecs.open("check_de_result.txt", "+w", encoding="utf-8")

    for dirs, folders, files in os.walk(url):
        for folder in folders:
            if folder.startswith("Folder_"):
                countWAV = 0
                # countAnt = 0
                # countAntx = 0
                countTxt = 0
                countAtt = 0
                countSeg = 0
                countCsv = 0
                path = os.path.join(dirs, folder)
                for dirs2, folders2, files2 in os.walk(path):
                    if len(folders2) > 0:
                        rs.write(path + "\\" + "folder lồng nhau" + "\n")
                        break
                    else:
                        try:
                            num_folder = int(folder.lstrip("Folder_"))
                            num_max = num_folder * 21
                            num_min = (num_folder - 1) * 21
                            for file in files2:
                                if file.endswith(".wav"):
                                    countWAV += 1
                                    num_file = int(file.lstrip("task2_").rstrip(".wav"))
                                    if num_file > num_max or num_file < num_min:
                                        rs.write(path + "\\" + "Sai file trong folder" + "\n")
                                        break
                                # if file.endswith("ant"):
                                #     countAnt += 1
                                # if file.endswith("antx"):
                                #     countAntx += 1
                                if file.endswith("txt"):
                                    countTxt += 1
                                if file.endswith("attribute.csv"):
                                    countAtt += 1
                                if file.endswith("seg.csv"):
                                    countSeg += 1
                                if file.endswith("csv"):
                                    countCsv += 1
                            if countWAV < 21:
                                x = 21 - countWAV
                                rs.write(path + "\\" + "Thiếu WAV" + "\\" + str(x) + "\n")
                            if countWAV > 21:
                                x = countWAV - 21
                                rs.write(path + "\\" + "Thừa WAV" + "\\" + str(x) + "\n")
                            # if countAntx < 21:
                            #     x = 21 - countAntx
                            #     rs.write(path + "\\" + "Thiếu ANTX" + "\\" + str(x) + "\n")
                            # if countAntx > 21:
                            #     x = countAntx - 21
                            #     rs.write(path + "\\" + "Thừa ANTX" + "\\" + str(x) + "\n")
                            # if countAnt > 0:
                            #     rs.write(path + "\\" + "Thừa ANT" + "\\" + str(countAnt) + "\n")
                            if countTxt < 21:
                                x = 21 - countTxt
                                rs.write(path + "\\" + "Thiếu TEXT" + "\\" + str(x) + "\n")
                            if countTxt > 21:
                                x = countTxt - 21
                                rs.write(path + "\\" + "Thừa TEXT" + "\\" + str(x) + "\n")
                            if countAtt != countWAV:
                                rs.write(path + "\\" + "Lệch Attribute" + "\\" + str(countWAV-countAtt) + "\n")
                            if countSeg != countWAV:
                                rs.write(path + "\\" + "Lệch Segment" + "\\" + str(countWAV-countSeg)  + "\n")
                            if (countCsv / 2) != countWAV:
                                rs.write(path + "\\" + "Lệch Csv" + "\n")
                        except BaseException as BE:
                            print(path + "\\" + "{}".format(BE))
            else:
                rs.write(os.path.join(dirs, folder) + "\\" + "Sai tên folder" + "\n")


print(url_org)
check_de(url_org)
print("Xong de")
check_att(url_org)