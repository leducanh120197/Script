import os
import codecs

url = r"\\server10\NIPA\Fighting\Output-Sang"
rs = codecs.open("count_images_text_result.txt", "+w", encoding="utf-8")

for dirs, folders, files in os.walk(url):
    for folder in folders:
        if folder.count("_") == 2:
            path = os.path.join(dirs, folder)
            countImages = 0
            countText = 0
            for dirs2, folders2, files2 in os.walk(path):
                if len(folders2) > 0:
                    print(path + " : " + "folder nested")
                    break
                else:
                    for file in files2:
                        if file.endswith("txt"):
                            countText += 1
                        elif file.endswith("jpg"):
                            countImages += 1

                    rs.write(folder + " " + str(countImages) + " " + str(countText) + "\n")



