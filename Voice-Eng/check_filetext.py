import os

url = r"\\server10\NIPA\Voice_Eng\Phase_02"
print((url))

for dirs, folders, filenames in os.walk(url):
    for filename in filenames:
        if filename.endswith(".txt"):
            path = os.path.join(dirs, filename)
            full_text = open(path, encoding="utf-8-sig").read()
            # print(full_text)
            if full_text.__contains__("\n") or full_text.__contains__("  ") or full_text.__contains__("\t"):
                print(path)