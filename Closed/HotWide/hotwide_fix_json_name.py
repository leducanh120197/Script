import os

url = r""

for dp, fd, files in os.walk(url):
    for file in files:
        if not file.endswith(".txt"):
            continue
        if ".jpg" in file:
            new_name = file.replace(".jpg", "")
        elif ".png" in file:
            new_name = file.replace(".png", "")
        elif ".jpeg" in file:
            new_name = file.replace(".jpeg", "")
        elif ".jfif" in file:
            new_name = file.replace(".jfif", "")
        elif ".gif" in file:
            new_name = file.replace(".gif", "")
        else:
            continue
        os.rename(os.path.join(dp, file), os.path.join(dp, new_name))
