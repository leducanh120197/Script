import os
import codecs

url = r""

rs = codecs.open("count_not_text_result.txt", "w", "utf-8")
for dir, folders, files in os.walk(url):
    for folder in folders:
        if folder.__contains__("-"):
            if folder.__contains__("_"):
                path = os.path.join(dir, folder)
                for dirpath, f, filenames in os.walk(path):
                    count = 0
                    for filename in filenames:
                        if filename.endswith(".txt"):
                            count += 1
                    if count < 50:
                        rs.write(folder + " : " + str(count) + "\n")

