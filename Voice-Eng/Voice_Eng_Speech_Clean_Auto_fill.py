import os
import csv

url = r"C:\Users\LQA\OneDrive\Máy tính\Folder_507"
# url = r"\\server10\NIPA\Voice_Eng\Final_result\ChucNT_error\x"

for d, fds, fls in os.walk(url):
    for fl in fls:
        temp = []
        if not fl.endswith("_seg.csv"):
            continue
        path = os.path.join(d, fl)
        temp_file = os.path.join(d, fl + "temp.csv")
        try:
            with open(path, "r") as csv_file:
                reader = csv.reader(csv_file, delimiter=",")
                a = list(reader)
                temp.append(a[0])
                for i in range(1, len(a)):
                    for j in range(1, len(a[i])):
                        a[i][j] = a[i][j].strip()
                    if len(a[i]) == 3:
                        a[i].append("speech_clean")
                    else:
                        a[i][3] = "speech_clean"
                    temp.append(a[i])
            with open(temp_file, "w+", newline="") as fr:
                writer = csv.writer(fr, delimiter=",")
                for row in temp:
                    writer.writerow(row)
            os.remove(path)
            os.rename(temp_file, path)
        except BaseException as BE:
            print(path + "{}".format(BE))
