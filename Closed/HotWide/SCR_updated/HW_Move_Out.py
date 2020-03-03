import os
import shutil

url = r""

for dirs, folders, files in os.walk(url):
    for folder in folders:
        if not folder.startswith("-t"):
            continue
        path = os.path.join(dirs, folder)
        for d, fds, fls in os.walk(path):
            for file in fls:
                if file.endswith(".png"):
                    destination = os.path.join(os.path.dirname(path), file)
                    shutil.move(os.path.join(d, file), destination)
                elif file.endswith(".txt"):
                    destination = os.path.join(os.path.dirname(path), file)
                    shutil.move(os.path.join(d, file), destination)
        shutil.rmtree(path)
