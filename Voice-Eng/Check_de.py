import os
import codecs

url = r""

rs = codecs.open("check_de_result.txt", "+w", encoding="utf-8")

for dirs, folders, files in os.walk(url):
    for folder in folders:
        if folder.startswith("Folder_"):
            countWAV = 0
            countAnt = 0
            countAntx = 0
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
                            if file.endswith("ant"):
                                countAnt += 1
                            if file.endswith("antx"):
                                countAntx += 1
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
                            rs.write(path + "\\" + "Thiếu WAV" + "\\" + str(x) +  "\n")
                        if countWAV > 21:
                            x = countWAV - 21
                            rs.write(path + "\\" + "Thừa WAV" + "\\" + str(x) + "\n")
                        if countAntx < 21:
                            x = 21 - countAntx
                            rs.write(path + "\\" + "Thiếu ANTX" + "\\" + str(x) +  "\n")
                        if countAntx > 21:
                            x = countAntx - 21
                            rs.write(path + "\\" + "Thừa ANTX" + "\\" + str(x) + "\n")
                        if countAnt > 0:
                            rs.write(path + "\\" + "Thừa ANT" + "\\" + str(countAnt) + "\n")
                        if countTxt < 21:
                            x = 21 - countTxt
                            rs.write(path + "\\" + "Thiếu TEXT" + "\\" + str(x) +  "\n")
                        if countTxt > 21:
                            x = countTxt - 21
                            rs.write(path + "\\" + "Thừa TEXT" + "\\" + str(x) + "\n")
                        if countAtt != countAntx:
                            rs.write(path + "\\" + "Lệch Attribute" + "\n")
                        if countSeg != countAntx:
                            rs.write(path + "\\" + "Lệch Segment" + "\n")
                        if (countCsv/2) != countAntx:
                            rs.write(path + "\\" + "Lệch Csv" + "\n")
                    except BaseException as BE:
                        print(path + "\\" + "{}".format(BE))
        else:
            rs.write(os.path.join(dirs, folder) + "\\" + "Sai tên folder" + "\n")
