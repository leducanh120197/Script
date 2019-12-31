import os
import codecs

url = r"\\server10\Voice\Output"

rs = codecs.open("check_output_result.txt", "+w", encoding="utf-8")
done = codecs.open("check_output_input.txt", encoding="utf-8").read().splitlines()
upload = []

for dirs, folders, files in os.walk(url):
    for folder in folders:
        if folder.startswith("Folder_"):
            countWAV = 0
            countAnt = 0
            countTxt = 0
            countCSV = 0
            countStrange = 0
            upload.append(folder)
            path = os.path.join(dirs, folder)
            for dirs2, folders2, files2 in os.walk(path):
                if len(folders2) > 0:
                    # print(path + " : " + "folder lồng nhau")
                    rs.write(path + "\\" + "folder lồng nhau" + "\n")
                    break
                else:
                    try:
                        num_folder = int(folder.lstrip("Folder_"))
                        num_max = num_folder * 21
                        num_min = (num_folder - 1) * 21
                        for file in files2:
                            if file.endswith(".wav"):
                                num_file = int(file.lstrip("task2_").rstrip(".wav"))
                                if num_file > num_max or num_file < num_min:
                                    # print(path + " : " + " Sai file trong folder")
                                    rs.write(path + "\\" + "Sai file trong folder" + "\n")
                                    break
                        for file in files2:
                            if file.endswith("wav"):
                                countWAV += 1
                            elif file.endswith("ant"):
                                countAnt += 1
                            elif file.endswith("antx"):
                                countAnt += 1
                            elif file.endswith("txt"):
                                countTxt += 1
                            elif file.endswith("csv"):
                                countCSV += 1
                            else:
                                countStrange += 1

                        if countWAV < 21:
                            x = 21 - countWAV
                            rs.write(path + "\\" + "Thiếu WAV" + "\\" + str(x) +  "\n")
                        if countWAV > 21:
                            x = countWAV - 21
                            rs.write(path + "\\" + "Thừa WAV" + "\\" + str(x) + "\n")
                        if countAnt < 21:
                            x = 21 - countAnt
                            rs.write(path + "\\" + "Thiếu ANT" + "\\" + str(x) +  "\n")
                        if countAnt > 21:
                            x = countAnt - 21
                            rs.write(path + "\\" + "Thừa ANT" + "\\" + str(x) + "\n")
                        if countTxt < 21:
                            x = 21 - countTxt
                            rs.write(path + "\\" + "Thiếu TEXT" + "\\" + str(x) +  "\n")
                        if countTxt > 21:
                            x = countTxt - 21
                            rs.write(path + "\\" + "Thừa TEXT" + "\\" + str(x) + "\n")
                        if countCSV > 0:
                            rs.write(path + "\\" + "Thừa CSV" + "\n")
                        if countStrange > 0:
                            rs.write(path + "\\" + "Có file lạ" + "\n")
                    except BaseException as BE:
                        print(path + "{}".format(BE))
        # else:
        #     rs.write(dirs + "\\" + folder + "\\" + "Sai tên folder" + "\\" + "\n")
for item in done:
    if item not in upload:
        rs.write(item + "\\" + "Chưa upload" + "\n")