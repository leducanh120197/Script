import os
import json

url = r"\\server10\NIPA\2.Tranning\Output\1024"
fr = open("result.txt", "w+", encoding="utf-8-sig")

for dirs, folders, files in os.walk(url):
    for file in files:
        if not file.endswith(".json"):
            continue
        path = os.path.join(dirs, file)
        # fr.write(path + "\n")
        countError = 0
        with open(path) as fin:
            json_data = json.load(fin)
            imsize = json_data['imsize']
            for key, value in json_data['human_annotations'].items():
                item = json_data['human_annotations'][key]
                body_box = item.get('body_box')
                belonging = item.get('belongings')
                head_box = item.get('head_box')
                face_box = item.get('face_box')
                face_landmarks = item.get('face_landmarks')
                keypoints = item.get('keypoints')

                # Check thieu truncate body_box
                if len(body_box) < 4:
                    fr.write(path + "Cham thieu diem body_box" + "\n")
                elif body_box[0] == 0 or body_box[1] == 0 or body_box[2] == imsize[0] or body_box[3] == imsize[1]:
                    if item.get('truncated') == "none":
                        fr.write("\\\\\\\\\\\\\\\\\\(Error) PersonID %s: Body_box thieu Truncated" % key[-4:] + "\n")
                        countError += 1
                else:
                    if item.get('truncated') != "none":
                        fr.write("\\\\\\\\\\\\\\\\\\(Error) PersonID %s: Body_box sai Truncated" % key[-4:] + "\n")
                        countError += 1
                # Check thieu head_box
                if not head_box:
                    if face_box != [0, 0, 0, 0]:
                        fr.write("\\\\\\\\\\\\\\\\\\(Error) PersonID %s: Thieu head_box" % key[-4:] + "\n")
                        countError += 1
                # Check ve 2 box ko sat nhau
                if head_box:
                    if face_box != [0, 0, 0, 0]:
                        if body_box[1] != head_box[1] or head_box[3] != face_box[3]:
                            fr.write("\\\\\\\\\\\\\\\\\\(Error) PersonID %s: Ve box chua sat" % key[-4:] + "\n")
                            countError += 1
                    elif body_box[1] != head_box[1]:
                        fr.write("\\\\\\\\\\\\\\\\\\(Error) PersonID %s: Ve box chua sat" % key[-4:] + "\n")
                        countError += 1
                # Check thieu face_blur
                if item.get('face_blur') == str(2):
                    for mark in face_landmarks:
                        if not (mark == [-1, -1, -1] or mark == [-1, -1, 0]):
                            fr.write("\\\\\\\\\\\\\\\\\\(Error) PersonID %s: Sai face_blur" % key[-4:] + "\n")
                            countError += 1
                            break
                elif item.get('face_blur') == str(0):
                    count = 0
                    for mark in face_landmarks:
                        if not (mark == [-1, -1, -1] or mark == [-1, -1, 0]):
                            count += 1
                    if count == 0:
                        fr.write("\\\\\\\\\\\\\\\\\\(Error) PersonID %s: Thieu face_landmarks" % key[-4:] + "\n")
                        countError += 1
                # Check ve point lech
                for no, face_landmark in enumerate(face_landmarks):
                    if face_landmark == [-1, -1, -1]:
                        continue
                    if face_landmark == [-1, -1, 0]:
                        continue
                    if not face_landmark[0] in range(face_box[0]-1, face_box[2]+1) and face_landmark[1] in range(face_box[1]-1, face_box[3]+1):
                        fr.write("\\\\\\\\\\\\\\\\\\(Error) PersonID %s: %s: Face_landmark out of face_box" % (key[-4:], no+1) + "\n")
                        countError += 1
                for no, keypoint in enumerate(keypoints):
                    if keypoint == [-1, -1, -1]:
                        continue
                    if keypoint == [-1, -1, 0]:
                        continue
                    if not keypoint[0] in range(body_box[0]-1, body_box[2]+1) and keypoint[1] in range(body_box[1]-1, body_box[3]+1):
                        fr.write("\\\\\\\\\\\\\\\\\\(Error) PersonID %s: %s: Keypoint out of body_box" % (key[-4:], no+1) + "\n")
                        countError += 1
        if countError > 0:
            fr.write(path + "\n")

