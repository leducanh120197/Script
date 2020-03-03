# import pandas as pd
# xl = pd.ExcelFile('requestment.xlsx')
# # get the first sheet as an object
# df = pd.read_excel(xl, 0)
# # print(df.head())
# a = df.iloc[:, 0]
# for i in a:
#     print(type(i))

# import xlrd
# file_location = 'requestment.xlsx'
# wb = xlrd.open_workbook(file_location)
# sheet = wb.sheet_by_index(0)

# for rows in range(sheet.nrows):
#     print(str(sheet.cell_value(rows, 1)))



# def get_extract_list(url):
#     list_dict = {}
#     file_location = url
#     wb = xlrd.open_workbook(file_location)
#     sheet = wb.sheet_by_index(0)
    
#     for rows in range(sheet.nrows):
#         name = str(sheet.cell_value(rows, 1))
#         # name = name[:-(len(name)-name.rfind("."))]
#         time = sheet.cell_value(rows, 3)
#         list_dict[name] = time
#     return list_dict

# url = r"D:\GettyImages_Clips.xlsx"

# a = get_extract_list(url)
# print(a)

# import xlrd
# def get_duration(var):
#     var = var[:1]
#     return var
# a = get_duration("2 fps")
# print(a)




# print(os.path.basename("D:\HBLAB_getty\video\GettyImages-626713732"))

def get_framerate(var):
    # var = video_cap.get(cv2.CAP_PROP_FPS)
    rs = int(var)
    if rs < var:
        rs = rs + 1
    return rs

a = get_framerate(59.01)
print(a)