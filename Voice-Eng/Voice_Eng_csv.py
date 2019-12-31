import csv
import os
import shutil

url = r"C:\Users\LQA\OneDrive\Máy tính\Folder_507"
# url = r"\\server10\NIPA\Voice_Eng\Final_result\temple"
att = r"C:\Users\LQA\OneDrive\Máy tính\Script\Voice-Eng\sample_attribute.csv"
seg = r"C:\Users\LQA\OneDrive\Máy tính\Script\Voice-Eng\sample_seg.csv"

# url = r"C:\Users\leduc\Desktop\Folder_80"
# att = r"sample_attribute.csv"
# seg = r"sample_seg.csv"

for dirs, folders, files in os.walk(url):
    for file in files:
        if not file.endswith(".csv"):
            continue
        path = os.path.join(dirs, file)
        seg_path = os.path.join(dirs, os.path.splitext(file)[0] + "_seg.csv")
        att_path = os.path.join(dirs, os.path.splitext(file)[0] + "_attribute.csv")
        shutil.copy(att, att_path)
        shutil.copy(seg, seg_path)
        try:
            with open(path, encoding="utf-8") as csv_file:
                ct = csv.reader(csv_file, delimiter=",")
                starts = []
                ends = []
                labels = []
                values = []
                for row in ct:
                    for no, data in enumerate(row):
                        obj = data.split("\t")
                        start = int(obj[6])
                        end = start + int(obj[8])
                        label = obj[12]

                        starts.append(start)
                        ends.append(end)
                        labels.append(label)
            csv_file.close()
            with open(seg_path, "a") as csv_output:
                for x in range(0, len(starts)):
                    csv_output.write("%s, %.0f, %.0f\n" % (labels[x], starts[x], ends[x]))
            os.remove(path)
        except BaseException as BE:
            print(path + "{}".format(BE))
