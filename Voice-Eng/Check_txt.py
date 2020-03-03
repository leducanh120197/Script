import xml.dom.minidom
import os
import codecs
import re
import datetime

url = r"\\server10\Voice\Output"
# url = r"\\server10\NIPA\Voice_Eng\Phase_03\output-11"
# url = r"\\server10\NIPA\Voice_Eng\Phase_03\output-4"
rs = codecs.open("check_txt_result.txt", "+w", encoding="utf-8")

except_list = []

print(datetime.datetime.now())


def change_label(var):
    new_var = str(var).lower().strip()
    new_var = rm_escape(new_var)
    rs = re.sub("[^A-Za-z ]", "", new_var)
    return rs


def rm_escape(var):
    var = str(var).replace("\n","").replace("\t", "")
    return var

tab = "\\"
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
                        rs.write(dirs + tab + fileNum + tab + "Có từ ghép" + tab + x + tab + y + tab + str(text_list) + tab +  str(txt_segment) + "\n")
                else:
                    if x != set_null and y != set_null:
                        rs.write(dirs + tab + fileNum + tab + "Sai từ" + tab + x + tab + y + tab + str(text_list) + tab +  str(txt_segment) + "\n")
                    elif x != set_null and y == set_null:
                        rs.write(dirs + tab + fileNum + tab + "Thừa từ" + tab + x + tab + "" + tab + str(text_list) + tab +  str(txt_segment) + "\n")
                    elif x == set_null and y != set_null:
                        rs.write(dirs + tab + fileNum + tab + "Thiếu từ" + tab + "" + tab + y + tab + str(text_list) + tab +  str(txt_segment) + "\n")
                    else:
                        if len(txtSegment_oneline) > len(text_oneline):
                            rs.write(dirs + tab + fileNum + tab + "_Có thêm từ" + tab + "" + tab + "" + tab + str(text_list) + tab +  str(txt_segment) + "\n")
                        else:
                            rs.write(dirs + tab + fileNum + tab + "_Thiếu từ" + tab + "" + tab + "" + tab + str(text_list) + tab +  str(txt_segment) + "\n")
                # print(txtSegment_oneline)
                # print(text_oneline)

            except BaseException as BE:
                x = path + "\\" + "{}".format(BE)
                except_list.append(x)
for i in except_list:
    rs.write(i + "\n")

print(datetime.datetime.now())
