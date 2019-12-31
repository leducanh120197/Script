import os
import codecs

url = r"\\server10\NIPA\Voice_labeling\Output"

list_fd = open('not_upload_input.txt', encoding="utf-8").read().splitlines()
result = codecs.open('not_upload_result.txt', 'w+', 'utf-8-sig')
uploaded_fd = []

for dirs, folders, files in os.walk(url):
    for folder in folders:
        uploaded_fd.append(folder)
for item in list_fd:
    if item not in uploaded_fd:
        result.write(item + "\n")