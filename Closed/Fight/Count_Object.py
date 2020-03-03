import os

url = r"C:\Users\leduc\Desktop\server\Fight"

fr = open("count_object_result.txt", "w+", encoding="utf-8-sig")

for dirs, folders, files in os.walk(url):
    for folder in folders:
        if folder.count("_") == 2:
            path = os.path.join(dirs, folder)
            for dirs2, folders2, files2 in os.walk(path):
                if len(folders2) > 0:
                    print(path + " : " + "folder nested")
                    break
                count = 0
                for file in files2:
                    if file.endswith(".txt"):
                        file_path = os.path.join(dirs2, file)
                        try:
                            with open(file_path, "r") as fl:
                                text = fl.readlines()
                                count = count + len(text)
                        except:
                            print(file_path + ": Không đếm được")
                fr.write("%s:%s\n" % (os.path.basename(path), count))
