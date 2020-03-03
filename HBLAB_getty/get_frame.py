import cv2
import os
import codecs


rs = codecs.open("get_frame_rs_rs.txt", "+w", encoding="utf-8")
url = r"\\server10\Hblab\1.Customer\1.Video"

for dirs, folders, filenames in os.walk(url):
        for file in filenames:
            if file.endswith('.mov'):
                path = os.path.join(dirs, file)
                try:
                    vidcap = cv2.VideoCapture(path)
                    video_fps = vidcap.get(cv2.CAP_PROP_FPS)
                    rs.write(dirs + "\\" + file + "\\{:02f}\n".format(video_fps))
                except BaseException as BE:
                    rs.write("EXCEPT " + "\\" + file + "\n")