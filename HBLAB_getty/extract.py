import os
import cv2
import time
import codecs
import tkinter as tk

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


def extract_vid(url_in, url_out, filename, txt_log):
    try:
        os.mkdir(url_out)
    except OSError:
        pass

    time_start = time.time()
    vidcap = cv2.VideoCapture(url_in)

    video_length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    # # vidcap.set(cv2.CAP_PROP_POS_AVI_RATIO, 1)
    video_msc = int(vidcap.get(cv2.CAP_PROP_POS_MSEC))

    print("Duration in miliseconds", video_msc)
    print("Number of frames: ", video_length)
    txt_log.write("\tDuration in miliseconds: {} \n".format(video_msc))
    txt_log.write("\tNumber of frames: {} \n".format(video_length))

    success, image = vidcap.read()
    print(success)
    count_frame = 0
    curent_frame = 0
    while success:
        # creat image name
        filename_new = url_out + '\\' + filename + "_{:05d}.jpg".format(count_frame + 1)
        print(filename_new)

        # filename_new = 'frame%d.jpg' % count_frame
        # print(filename_new)

        cv2.imwrite(filename_new, image)
        # cv2.imshow(filename_new, image)

        success, image = vidcap.read()
        count_frame += 1
        curent_frame += 12
        if curent_frame > (video_length-1):
            # Log the time again
            time_end = time.time()
            # Release the feed
            vidcap.release()
            # Print stats

            print ("Done extracting frames: %d frames extracted" % count_frame)
            print ("It took %d seconds forconversion." % (time_end-time_start))
            txt_log.write("\tDone extracting frames: {:d}\n".format(count_frame))
            txt_log.write("\tIt took {:f} seconds forconversion.\n".format(time_end-time_start))
            break


def crop(url_in, url_out):
    url_log = url_in + "\log.txt"
    txt_log = codecs.open(url_log, "+w", encoding="utf-8")
    for dirs, folders, filenames in os.walk(url_in):
        for file in filenames:
            if file.endswith('.mov'):
                txt_log.write("- " + file + "\n")
                filename = file.rstrip('.mov')
                path_vid = os.path.join(dirs, file)
                path_out = os.path.join(url_out, filename)
                print(path_vid)
                extract_vid(path_vid, path_out, filename, txt_log)


def main():
    if check_url(txt_input.get()):
        url_input = txt_input.get()
        url_output = txt_output.get()
        crop(url_input, url_output)
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
