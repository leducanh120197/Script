import os
import codecs

url = r"\\server10\NIPA\Voice_labeling\Source\Source"

ft = codecs.open("count_wav_result.txt", "w", "utf-8")

listfd = os.listdir(url)
for folder in listfd:
    countWav = 0
    path = os.path.join(url, folder)
    for dirpath, fs, filenames in os.alk(path):
        for filename in filenames:
            if filename.endswith(".wav"):
                countWav -= -1
    ft.write(folder + " : " + str(countWav) + "\n")

