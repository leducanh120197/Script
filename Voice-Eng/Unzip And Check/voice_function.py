import xml.dom.minidom
import zipfile
import datetime
import os
import codecs
import re

tab = "\t"

def unzip(url):
    print(str(datetime.datetime.now()) + " Unzip ant => antx: Doing")
    for dirs, folders, files in os.walk(url):
        for file in files:
            if file.endswith(".ant"):
                try:
                    with zipfile.ZipFile(os.path.join(dirs,file)) as Zip:
                        for Zip_info in Zip.infolist():
                            if Zip_info.filename[-1] == '/':
                                continue
                            Zip_info.filename = file + "x"
                            Zip.extract(Zip_info, dirs)
                    os.remove(os.path.join(dirs,file))
                except BaseException as BE:
                    print(dirs + tab + file + tab + "{}".format(BE))
    print(str(datetime.datetime.now()) + " Unzip ant => antx: Done")


def check_folder(url):
    print(str(datetime.datetime.now()) + " Checking folder: Doing")
    url_new = url + "\check_folders_result.txt"
    # url_new = url[:-(len(url)-url.rfind("\\"))] + "\check_folders_result.txt"
    rs = codecs.open(url_new, "+w", encoding="utf-8")
    countERROR = 0
    for dirs, folders, files in os.walk(url):
        for folder in folders:
            if folder.startswith("Folder_"):
                countWAV = 0
                countAnt = 0
                countAntx = 0
                countTxt = 0
                countCSV = 0
                countStrange = 0
                path = os.path.join(dirs, folder)
                for dirs2, folders2, files2 in os.walk(path):
                    if len(folders2) > 0:
                        rs.write(folder + tab + "folder lồng nhau" + "\n")
                        countERROR += 1
                        break
                    else:
                        try:
                            num_folder = int(folder.lstrip("Folder_"))
                            num_max = num_folder * 21
                            num_min = (num_folder - 1) * 21
                            for file in files2:
                                if file.endswith(".wav"):
                                    num_file = int(file.lstrip("task2_").rstrip(".wav"))
                                    if num_file > num_max or num_file < num_min:
                                        rs.write(folder + tab + "Sai file trong folder" + "\n")
                                        countERROR += 1
                                        break
                            for file in files2:
                                if file.endswith("wav"):
                                    countWAV += 1
                                elif file.endswith("ant"):
                                    countAnt += 1
                                elif file.endswith("antx"):
                                    countAntx += 1
                                elif file.endswith("txt"):
                                    countTxt += 1
                                elif file.endswith("csv"):
                                    countCSV += 1
                                else:
                                    countStrange += 1

                            if countWAV < 21:
                                x = 21 - countWAV
                                rs.write(folder + tab + "Thiếu WAV" + tab + str(x) +  "\n")
                                countERROR += 1
                            if countWAV > 21:
                                x = countWAV - 21
                                rs.write(folder + tab + "Thừa WAV" + tab + str(x) + "\n")
                                countERROR += 1
                            if countAnt > 0:
                                rs.write(folder + tab + "Còn ANT" + tab + str(countAnt) + "\n")
                                countERROR += 1
                            if countAntx < 21:
                                x = 21 - countAntx
                                rs.write(folder + tab + "Thiếu ANTX" + tab + str(x) +  "\n")
                                countERROR += 1
                            if countAntx > 21:
                                x = countAntx - 21
                                rs.write(folder + tab + "Thừa ANTX" + tab + str(x) + "\n")
                                countERROR += 1
                            if countTxt < 21:
                                x = 21 - countTxt
                                rs.write(folder + tab + "Thiếu TEXT" + tab + str(x) +  "\n")
                                countERROR += 1
                            if countTxt > 21:
                                x = countTxt - 21
                                rs.write(folder + tab + "Thừa TEXT" + tab + str(x) + "\n")
                                countERROR += 1
                            if countCSV > 0:
                                rs.write(folder + tab + "Thừa CSV" + "\n")
                                countERROR += 1
                            if countStrange > 0:
                                rs.write(folder + tab + "Có file lạ" + "\n")
                                countERROR += 1
                        except BaseException as BE:
                            print(path + "{}".format(BE))
    print("có {} lỗi".format(countERROR))
    if countERROR == 0:
        rs.write("Không có lỗi")
    print(str(datetime.datetime.now()) + " Checking folder: Done")


def change_label(var):
    new_var = str(var).lower().strip()
    new_var = rm_escape(new_var)
    rs = re.sub("[^A-Za-z ]", "", new_var)
    return rs


def rm_escape(var):
    var = str(var).replace("\n","").replace(tab, "")
    return var


def check_text(url):
    print(str(datetime.datetime.now()) + " Checking text: Doing")
    countERROR = 0
    url_new = url + "\check_text_result.txt"
    rs = codecs.open(url_new, "+w", encoding="utf-8")
    except_list = []
    for dirs, folders, files in os.walk(url):
        for file in files:
            if file.endswith("antx"):
                fileNum = file.rstrip(".antx")
                try:
                    text_list = list(open(os.path.join(dirs, fileNum + ".txt"), "r", encoding="utf-8").read().split(" "))
                    text_oneline = open(os.path.join(dirs, fileNum + ".txt"), "r", encoding="utf-8").read().replace("\n", "").replace(" ", "")

                    txt_segment = []
                    path = os.path.join(dirs, file)
                    DOMTree = xml.dom.minidom.parse(path)
                    collection = DOMTree.documentElement

                    Segments = collection.getElementsByTagName("Segment")
                    for segment in Segments:
                        label = segment.getElementsByTagName("Label")[0].childNodes[0].data
                        new_label = change_label(label)
                        txt_segment.append(new_label)

                    txtSegment_oneline = ''.join(txt_segment).replace(" ", "")
                    x = str(set(txt_segment) - set(text_list))
                    y = str(set(text_list) - set(txt_segment))
                    set_null = "set()"
                    if txtSegment_oneline == text_oneline:
                        if x != set_null and y != set_null:
                            rs.write(dirs + tab + fileNum + tab + "Có từ ghép" + tab + x + tab + y + tab + str(text_list) + tab + str(txt_segment) + "\n")
                            countERROR += 1
                    else:
                        if x != set_null and y != set_null:
                            rs.write(dirs + tab + fileNum + tab + "Sai từ" + tab + x + tab + y + tab + str(text_list) + tab + str(txt_segment) + "\n")
                            countERROR += 1
                        elif x != set_null and y == set_null:
                            rs.write(dirs + tab + fileNum + tab + "Thừa từ" + tab + x + tab + "" + tab + str(text_list) + tab + str(txt_segment) + "\n")
                            countERROR += 1
                        elif x == set_null and y != set_null:
                            rs.write(dirs + tab + fileNum + tab + "Thiếu từ" + tab + "" + tab + y + tab + str(text_list) + tab + str(txt_segment) + "\n")
                            countERROR += 1
                        else:
                            if len(txtSegment_oneline) > len(text_oneline):
                                rs.write(dirs + tab + fileNum + tab + "_Có thêm từ" + tab + "" + tab + "" + tab + str(text_list) + tab + str(txt_segment) + "\n")
                                countERROR += 1
                            else:
                                rs.write(dirs + tab + fileNum + tab + "_Thiếu từ" + tab + "" + tab + "" + tab + str(text_list) + tab + str(txt_segment) + "\n")
                                countERROR += 1
                except BaseException as BE:
                    x = dirs + tab + fileNum + tab + "{}".format(BE)
                    except_list.append(x)
    for i in except_list:
        rs.write(i + tab + "có thể có segment trống" + "\n")
    print("có {} lỗi".format(countERROR))
    if countERROR == 0:
        rs.write("Không có lỗi")
    print(str(datetime.datetime.now()) + " Checking text: Done")