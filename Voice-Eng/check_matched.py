import os
import codecs
import csv

# url_org = r"\\server10\NIPA\Voice_Eng\Phase_02-DELIVERED\part_01_3k"
url_org = r"\\server10\NIPA\Voice_Eng\Phase_02\part_02_5k"
print(url_org)

list_true = ["true", "TRUE"]
list_false = ["false", "FALSE"]


def find_and_replace(url):
    a = "\\"

    rs = codecs.open("check_matched_result.txt", "+w", encoding="utf-8")

    for dirs, folders, files in os.walk(url):
        for file in files:
            if file.endswith('.txt'):
                try:
                    path = os.path.join(dirs, file)
                    url_att = path.replace('.txt', '_attribute.csv')
                    url_seg = path.replace('.txt', '_seg.csv')

                    text_full = open(path, encoding="utf-8-sig").read().lower()

                    with open(url_seg) as csv_file:
                        segment_list = []
                        try:
                            readCSV = csv.reader(csv_file, delimiter=",")
                            next(readCSV)
                            for row in readCSV:
                                segment_list.append(str(row[0]).strip().lower())
                            segment_full = ' '.join(segment_list)
                        except BaseException as BE:
                            rs.write("EXCEPT" + a + os.path.join(dirs, file) + a + "{}".format(BE) + "\n")
                    csv_file.close()

                    with open(url_att) as csv_file:
                        try:
                            readCSV = list(csv.reader(csv_file, delimiter=","))
                            for row in readCSV:
                                if row[0] == "matched":
                                    # and (str(row[1]).strip() not in matched):
                                    matched = str(row[1]).lower().strip()
                                    break
                        except BaseException as BE:
                            rs.write("EXCEPT" + a + os.path.join(dirs, file) + a + "{}".format(BE) + "\n")
                    csv_file.close()
                    # rs.write("true" + a + path + "\n")

                    if text_full == segment_full and matched not in list_true:
                        try:
                            readCSV[1][1] = "true"
                            writer = csv.writer(open(url_att, 'w', newline=''))
                            writer.writerows(readCSV)
                        except BaseException as BE:
                            print("EXCEPT writer" + a + os.path.join(dirs, file) + a + "{}".format(BE))

                    elif text_full != segment_full and matched not in list_false:
                        try:
                            readCSV[1][1] = "false"
                            writer = csv.writer(open(url_att, 'w', newline=''))
                            writer.writerows(readCSV)
                        except BaseException as BE:
                            print("EXCEPT writer" + a + os.path.join(dirs, file) + a + "{}".format(BE))
                except BaseException as BE:
                    rs.write("EXCEPT" + a + os.path.join(dirs, file) + a + "{}".format(BE) + "\n")


def find(url):
    a = "\\"

    rs = codecs.open("check_matched_result.txt", "+w", encoding="utf-8")

    for dirs, folders, files in os.walk(url):
        for file in files:
            if file.endswith('.txt'):
                try:
                    path = os.path.join(dirs, file)
                    url_att = path.replace('.txt', '_attribute.csv')
                    url_seg = path.replace('.txt', '_seg.csv')

                    text_full = open(path, encoding="utf-8-sig").read().lower()

                    with open(url_seg) as csv_file:
                        segment_list = []
                        try:
                            readCSV = csv.reader(csv_file, delimiter=",")
                            next(readCSV)
                            for row in readCSV:
                                segment_list.append(str(row[0]).strip().lower())
                            segment_full = ' '.join(segment_list)
                        except BaseException as BE:
                            rs.write("EXCEPT" + a + os.path.join(dirs, file) + a + "{}".format(BE) + "\n")
                    csv_file.close()

                    with open(url_att) as csv_file:
                        try:
                            readCSV = list(csv.reader(csv_file, delimiter=","))
                            for row in readCSV:
                                if row[0] == "matched":
                                    # and (str(row[1]).strip() not in matched):
                                    matched = str(row[1]).lower().strip()
                                    break
                        except BaseException as BE:
                            rs.write("EXCEPT" + a + os.path.join(dirs, file) + a + "{}".format(BE) + "\n")
                    csv_file.close()

                    if text_full == segment_full and matched not in list_true:
                        rs.write("true" + a + path + "\n")
                    elif text_full != segment_full and matched not in list_false:
                        rs.write("false" + a + path + "\n")
                except BaseException as BE:
                    rs.write("EXCEPT" + a + os.path.join(dirs, file) + a + "{}".format(BE) + "\n")


# find_and_replace(url_org)
find(url_org)
