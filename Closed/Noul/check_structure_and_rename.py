import os
import shutil

url = r""

for dirpath, folders, filenames in os.walk(url):
    for filename in filenames:
        if filename.endswith(".db"):
            continue
        if filename.endswith(".ini"):
            continue

        foldername = os.path.basename(os.path.dirname(dirpath))
        basename = os.path.basename(dirpath)

        if basename.endswith(os.path.splitext(filename)[0]):
            if filename.endswith(".png"):
                os.makedirs(os.path.join(dirpath, "label"))
                shutil.move(os.path.join(dirpath, filename), os.path.join(dirpath, "label"))
            elif filename.endswith(".jpg"):
                os.makedirs(os.path.join(dirpath, "source"))
                shutil.move(os.path.join(dirpath, filename), os.path.join(dirpath, "source"))
            elif filename.endswith(".xcf"):
                os.makedirs(os.path.join(dirpath, "xcf"))
                shutil.move(os.path.join(dirpath, filename), os.path.join(dirpath, "xcf"))

        elif not foldername.endswith(os.path.splitext(filename)[0]):
            print(dirpath + " Anh va thu muc khong dong nhat")

        elif filename.endswith(".png") and not basename == "label":
            if os.path.exists(os.path.join(os.path.dirname(dirpath), "label")):
                shutil.move(os.path.join(dirpath, filename), os.path.join(os.path.dirname(dirpath), "label"))
            else:
                os.rename(dirpath, os.path.join(os.path.dirname(dirpath), "label"))
            print(dirpath + "fixed")

        elif filename.endswith(".jpg") and not basename == "source":
            if os.path.exists(os.path.join(os.path.dirname(dirpath), "source")):
                shutil.move(os.path.join(dirpath, filename), os.path.join(os.path.dirname(dirpath), "source"))
            else:
                os.rename(dirpath, os.path.join(os.path.dirname(dirpath), "source"))
            print(dirpath + "fixed")

        elif filename.endswith(".xcf") and not basename == "xcf":
            if os.path.exists(os.path.join(os.path.dirname(dirpath), "xcf")):
                shutil.move(os.path.join(dirpath, filename), os.path.join(os.path.dirname(dirpath), "xcf"))
            else:
                os.rename(dirpath, os.path.join(os.path.dirname(dirpath), "xcf"))
            print(dirpath + "fixed")
        else:
            print(dirpath + " DONE")