import csv
import os
import shutil

url = r"C:\Users\LQA\OneDrive\Máy tính\car_horn_1902"
sample = r"C:\Users\LQA\OneDrive\Máy tính\Script\Voice\sample.csv"
baby_error = open(r"C:\Users\LQA\OneDrive\Máy tính\error list\baby_cry.txt").read().splitlines()
bark_error = open(r"C:\Users\LQA\OneDrive\Máy tính\error list\bark.txt").read().splitlines()
horn_error = open(r"C:\Users\LQA\OneDrive\Máy tính\error list\horn.txt").read().splitlines()
clap_error = open(r"C:\Users\LQA\OneDrive\Máy tính\error list\clap.txt").read().splitlines()
cough_error = open(r"C:\Users\LQA\OneDrive\Máy tính\error list\cough.txt").read().splitlines()
gun_error = open(r"C:\Users\LQA\OneDrive\Máy tính\error list\gun.txt").read().splitlines()
scream_error = open(r"C:\Users\LQA\OneDrive\Máy tính\error list\scream.txt").read().splitlines()
siren_error = open(r"C:\Users\LQA\OneDrive\Máy tính\error list\siren.txt").read().splitlines()
speech_error = open(r"C:\Users\LQA\OneDrive\Máy tính\error list\speech.txt").read().splitlines()

noise_error = open(r"C:\Users\LQA\OneDrive\Máy tính\error list\noise.txt").read().splitlines()

for dirs, folders, files in os.walk(url):
    for file in files:
        if not file.endswith(".csv"):
            continue
        path = os.path.join(dirs, file)
        new_path = os.path.join(dirs, os.path.splitext(file)[0] + "_rs.csv")
        os.rename(path, new_path)
        shutil.copy(sample, path)
        with open(new_path) as csv_file:
            ct = csv.reader(csv_file, delimiter=",")
            # next(ct)
            starts = []
            ends = []
            labels = []
            values = []
            for row in ct:
                for no, data in enumerate(row):
                    try:
                        obj = data.split("\t")
                        start = int(obj[6])
                        end = start + int(obj[8])
                        label = obj[12]
                        value = obj[9]

                        if label in baby_error:
                            label = "baby_cry"
                        elif label in bark_error:
                            label = "bark"
                        elif label in clap_error:
                            label = "clap"
                        elif label in cough_error:
                            label = "cough"
                        elif label in gun_error:
                            label = "gun"
                        elif label in horn_error:
                            label = "horn"
                        elif label in scream_error:
                            label = "scream"
                        elif label in siren_error:
                            label = "siren"
                        elif label in speech_error:
                            label = "speech"
                        elif value in noise_error:
                            value = "0"
                        starts.append(start)
                        ends.append(end)
                        labels.append(label)
                        values.append(value)
                    except BaseException as BE:
                        print(new_path + "{}".format(BE))
        csv_file.close()
        with open(path, "a") as csv_output:
            for x in range(0, len(starts)):
                csv_output.write("%s, %.0f, %.0f, %s\n" % (labels[x], starts[x], ends[x], values[x]))
        os.remove(new_path)
