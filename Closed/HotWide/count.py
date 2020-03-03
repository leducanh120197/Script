import os
import codecs

url = r""

rs = codecs.open("count_result.txt", "w", "utf-8")
for dir, folders, files in os.walk(url):
    for folder in folders:
        if folder.__contains__("-"):
            if folder.__contains__("_"):
                path = os.path.join(dir, folder)
                for dirpath, f, filenames in os.walk(path):
                    difference = 0
                    countImages = 0
                    countText = 0
                    countJson = 0
                    for filename in filenames:
                        if filename.endswith(".db"):
                            continue
                        elif filename.endswith(".ini"):
                            continue
                        elif filename.endswith(".txt"):
                            countText += 1
                        elif filename.endswith(".json"):
                            countJson += 1
                        else:
                            countImages += 1
                    difference = countImages - countText - countJson
                    if difference >= 0:
                        rs.write(path + " : " + folder + " : " + str(difference)+ " : " + str(countText) + "\n")
