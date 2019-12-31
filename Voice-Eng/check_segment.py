import os
import codecs
import csv

# url = r"C:\Users\LQA\OneDrive\Máy tính\New folder"
url = r"\\server10\NIPA\Voice_Eng\Phase_02\part_01_3k"
rs = codecs.open("check_segment_result.txt", "+w", encoding="utf-8")

for dirs, folders, files in os.walk(url):
    for file in files:
        if file.endswith(".txt"):
            filename = file.rstrip(".txt")
            segment = []
            text = open(os.path.join(dirs,file), "r", encoding="utf-8").read().replace("\n", "").replace(" ","")
            # print(text)
            for file2 in files:
                if file2 == (filename + "_seg.csv"):
                    with open(os.path.join(dirs, file2)) as csv_file:
                        readCSV = csv.reader(csv_file, delimiter=",")
                        next(readCSV)
                        for row in readCSV:
                            segment.append(row[0])
                        txtSegment = ''.join(segment)
                        # print(txtSegment)
            if text != txtSegment:
                rs.write(dirs + "\t" + filename + "\n")




