import os
import cv2
import time
import codecs
import tkinter as tk
import re
import xlrd
import function_extract

root= tk.Tk()
# root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file=r'.\download.png'))
root.title("LQA")


def check_url(input_url):
    var = os.path.isdir(input_url)
    return var


def print_status(var_str):
    label1 = tk.Label(root, text= var_str, fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)


def print_rs(var_str):
    label1 = tk.Label(root, text= var_str, fg='green', font=('helvetica', 10, 'bold'))
    canvas1.create_window(150, 230, window=label1)


def main():
    if check_url(txt_input.get()):
        url_input = txt_input.get()
        url_output = txt_output.get()
        function_extract.crop(url_input, url_output)
        print_status("Xem kết quả tại:")
        print_rs(url_output)
        print("FINISHED EXTRACT.")
    else:
        print_status("URL không hỗ trợ")


canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

# label input
lbl_input = tk.Label(root, text= "Input: ", font=('helvetica', 10))
canvas1.create_window(50, 80, window=lbl_input)
# text box input
txt_input = tk.Entry(root, width=30)
canvas1.create_window(160, 80, window=txt_input)

#label output
lbl_output = tk.Label(root, text= "Output: ", font=('helvetica', 10))
canvas1.create_window(50, 120, window=lbl_output)

# text box input
txt_output = tk.Entry (root, width=30)
canvas1.create_window(160, 120, window=txt_output)



button1 = tk.Button(text='Extract',command=main, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()
