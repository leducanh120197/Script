import os

url = r"\\172.16.8.10\Noul_Medical\Output_IMG_collection\Annotation_IMG\Output\Sep_03"

# url = r"C:\Users\leduc\Desktop\23"

fr = open("count_object_result.txt", "w+", encoding="utf-8-sig")

error_list = open("hw_count_object_error.txt", "w+", encoding="utf-8-sig")

for dirs, folders, files in os.walk(url):
    for folder in folders:
        if folder.__contains__("_"):
            if folder.__contains__("-"):
                path = os.path.join(dirs, folder)
                for d, fs, fls in os.walk(path):
                    count = 0
                    for file in fls:
                        if not file.endswith(".txt"):
                            continue
                        fp = os.path.join(d, file)
                        try:
                            with open(fp, "r") as fl:
                                text = fl.readlines()
                                count = count + len(text)
                        except FileNotFoundError:
                            error_list.write(fp + ": Ten dai qua" + "\n")
                        except UnicodeDecodeError:
                            error_list.write(fp + ": DecodeError ????" + "\n")
                    fr.write("%s:%s\n" % (os.path.basename(path), count))
