import os
import codecs

url = r"\\server10\NIPA\Voice_labeling\Output"

ft = codecs.open("count_wav_ant_csv.txt", "w", "utf-8")

for dirs, folders, files in os.walk(url):
    for folder in folders:
        if folder.__contains__("_"):
            countWav = 0
            countAnt = 0
            countCsv = 0
            path = os.path.join(dirs, folder)
            for dir2, folders2, files2 in os.walk(path):
                if len(folders2) > 0:
                    print(path + " : " + "folder nested")
                    break
                for file in files2:
                    if file.endswith("wav"):
                        countWav += 1
                    if file.endswith("ant"):
                        countAnt += 1
                    if file.endswith("csv"):
                        countCsv += 1
            ft.write(folder + " " + str(countWav) + " " + str(countAnt) + " " + str(countCsv) + "\n")
