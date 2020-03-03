import csv
import os
import codecs

# url = r"\\server10\NIPA\Voice_labeling\Rework"
# url = r"C:\Users\LQA\OneDrive\Máy tính\test"
# url = r"\\server10\NIPA\Voice_labeling\Rework2020\siren"
url = r"\\server10\NIPA\Voice_labeling\Rework-3rd\cough_02"
rs = codecs.open("check_csv_non_rs.txt", "+w", encoding="utf-8")
# error_list = codecs.open("error_list_rs.txt", "+w", encoding="utf-8")

noise = [" 0", " 1", " 2", " 3", "0", "1", "2", "3"]
segment = ["cough", "horn", "siren", "gun", "baby_cry", "scream", "clap", "bark", "speech"]

for dirs, folders, files in os.walk(url):
    for file in files:
        if file.endswith("csv"):
            with open(os.path.join(dirs, file)) as csv_file:
                try:
                    readCSV = csv.reader(csv_file, delimiter=",")
                    # if len(list(readCSV)) < 1:
                    #     rs.write(dirs + " : " + file + "\n")
                    next(readCSV)
                    for row in readCSV:
                        # print(row[0])
                        if str(row[0]) not in segment:
                            rs.write(dirs + " : " + file + " : " + "  CLASS  " + " : " + row[0] + "\n")
                        if str(row[3]) not in noise:
                            rs.write(dirs + " : " + file + " : " + "  NOISE  " + " : " + row[3] + "\n")
                except BaseException as BE:
                    print(dirs + file + "{}".format(BE))




