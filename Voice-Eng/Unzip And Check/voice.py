import os
import tkinter as tk
import voice_function

root= tk.Tk()
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file=r'.\download.png'))
root.title("LQA")


def check_url(input_url):
    var = os.path.isdir(input_url)
    return var


def print_status (var_str):
    label1 = tk.Label(root, text= var_str, fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)


def print_rs (var_str):
    label1 = tk.Label(root, text= var_str, fg='green', font=('helvetica', 10, 'bold'))
    canvas1.create_window(150, 230, window=label1)


def main():
    if check_url(entry1.get()):
        url = entry1.get()
        voice_function.unzip(url)
        voice_function.check_folder(url)
        voice_function.check_text(url)
        print_status("Xem kết quả tại:")
        # url_new = url[:-(len(url) - url.rfind("\\"))]
        print_rs(url)
        print("FINISHED CHECKING.")
    else:
        print_status("URL không hỗ trợ")


canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

label2 = tk.Label(root, text= "Nhập đường dẫn chứa folder:", font=('helvetica', 10))
canvas1.create_window(150, 80, window=label2)

entry1 = tk.Entry (root, width=27)
canvas1.create_window(150, 120, window=entry1)

button1 = tk.Button(text='Kiểm tra',command=main, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()
