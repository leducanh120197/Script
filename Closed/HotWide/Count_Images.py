import os
import codecs

url = r"\\172.16.8.10\Noul_Medical\Output_IMG_collection\Annotation_IMG\final_output"
list_fd = open('list.txt', encoding="utf-8").read().splitlines()
ft = codecs.open("count_images_result.txt", "w", "utf-8")
folders_in_output = []

for dir, folders, files in os.walk(url):
    for folder in folders:
        if folder in list_fd:
            if folder.__contains__("-"):
                if folder.__contains__("_"):
                    path = os.path.join(dir, folder)
                    for dirpath, f, filenames in os.walk(path):
                        count = 0
                        for filename in filenames:
                            if filename.endswith(".db"):
                                continue
                            elif filename.endswith(".ini"):
                                continue
                            elif filename.endswith(".txt"):
                                continue
                            elif filename.endswith(".json"):
                                continue
                            else:
                                count += 1
                        ft.write(folder + " : " + str(count) + "\n")
                        folders_in_output.append(folder)

with open("not_in_out.txt", "w", encoding="utf-8") as rf:
    for item in list_fd:
        if item not in folders_in_output:
            rf.write("%s\n" % item)