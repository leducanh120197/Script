import os
import codecs

url = r""

list_fd = open('not_upload_input.txt', encoding="utf-8").read().splitlines()
result = codecs.open('not_upload_result.txt', 'w+', 'utf-8-sig')
uploaded_fd = []

for dirs, folders, files in os.walk(url):
    for folder in folders:
        if folder.__contains__("-"):
            if folder.__contains__("_"):
                uploaded_fd.append(folder)
for item in list_fd:
    if item not in uploaded_fd:
        result.write("%s :CHUA UPLOAD\n" % item)
