import json
import os
import codecs

# url = r"C:\Users\LQA\OneDrive\Máy tính\test"
url = r"C:\Users\leduc\OneDrive\Máy tính\x\New folder"

# url_via_setting = r"/via_settings.json"
# url_via_attributes = r"/via_attributes.json"


# with open(url_via_setting, encoding="utf-8") as json_file:
#     via_setting = json.load(json_file)
# json_file.close()

# with open(url_via_attributes, encoding="utf-8") as json_file:
#     via_attributes = json.load(json_file)
# json_file.close()

via_img_metadata = []
for dirs, folders, filenames in os.walk(url):
    with open('data.json', 'w') as outfile:
        for filename in filenames:
            if filename.endswith("json"):
                path = os.path.join(dirs, filename)
                with open(path, encoding="utf-8") as json_file:
                    data = json.load(json_file)
                    try:
                        for name in data:
                            if name == "_via_img_metadata":
                                print(data[name])
                                print("--------------")
                                via_img_metadata += data[name]
                                print(via_img_metadata)
                                print("++++++++++++++")
                                json.dump(data[name], outfile, separators=(',', ':'))
                    except BaseException as BE:
                        print("{}".format(BE))
                json_file.close()
        # json.dump(via_img_metadata, outfile)
