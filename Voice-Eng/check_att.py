import os
import codecs
import csv

# url = r"\\server10\NIPA\Voice_Eng\Final_result"
url = r"\\server10\NIPA\Voice_Eng\Phase_02\part_05_5k"

matched = ["TRUE", "FALSE", "true", "false"]
tone = ["0", "1"]
speed = ["0", "1", "2"]
label = ["matched", "speaker_sex", "tone", "ATTRIBUTE", "speed"]
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
                            rs.write("matched" + a + dirs + a + file + "\n")
                        if row[0] == "speaker_sex" and (str(row[1]).strip() not in tone):
                            rs.write("speaker_sex" + a + dirs + a + file + "\n")
                        if row[0] == "tone" and (str(row[1]).strip() not in tone):
                            rs.write("tone" + a + dirs + a + file + "\n")
                        if row[0] == "speed" and (str(row[1]).strip() not in speed):
                                rs.write("speed" + a + dirs + a + file + "\n")
                        if str(row[0]).strip() not in label:
                            rs.write("label" + a + dirs + a + file + "\n")
                            # print("label" + a + dirs + file + "\n")
                        # if str(row).isspace():
                        #     rs.write("Dòng trống" + a + dirs + a + file + "\n")
                except BaseException as BE:
                    rs.write("EXCEPT" + a + os.path.join(dirs, file) + "{}".format(BE) + "\n")
            csv_file.close()

