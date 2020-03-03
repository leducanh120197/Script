import os
import codecs
# import time
import cv2
import xlrd


def get_start_frame(var, frame):
    var = int(var[2:4])
    start = var * frame
    return start


def get_end_frame(var, frame):
    var = int(var[9:11])
    end = var * frame
    return end


def get_framerate(video_cap):
    var = video_cap.get(cv2.CAP_PROP_FPS)
    rs = int(var)
    if rs < var:
        rs = rs + 1
    return rs


def get_fps(fps_str):
    fps = int(fps_str[:1])
    return fps


def get_jump_fps(fps, frame_rate):
    if int(frame_rate) < frame_rate:
        frame_rate = frame_rate + 1
    if fps == 2:
        jump = frame_rate / 2
        return jump
    if fps == 1:
        return frame_rate
    if fps == 3:
        if frame_rate == 25:
            return 10
        if frame_rate == 30:
            return 8
        if frame_rate == 60:
            return 20


def get_list_duration_fps(url):
    dict_duration = {}
    dict_fps = {}
    file_location = url
    wb = xlrd.open_workbook(file_location)
    sheet = wb.sheet_by_index(0)
    for rows in range(sheet.nrows):
        name = str(sheet.cell_value(rows, 2))
        duration = sheet.cell_value(rows, 4)
        fps = sheet.cell_value(rows, 5)
        dict_duration[name] = duration
        dict_fps[name] = fps
    return dict_duration, dict_fps


def extract_vid(vidcap, frame_rate, start_frame, end_frame, fps_str, path_out, filename, txt_log):
    video_length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    video_msc = int(vidcap.get(cv2.CAP_PROP_POS_MSEC))

    # write log
    print("Duration in miliseconds", video_msc)
    print("Number of frames: ", video_length)
    print("Frame : ", frame_rate)
    txt_log.write("\tDuration in miliseconds: {} \n".format(video_msc))
    txt_log.write("\tNumber of frames: {} \n".format(video_length))
    txt_log.write("\tFPS : {} \n".format(frame_rate))

    curent_frame = start_frame
    fps = get_fps(fps_str)
    jump_fps = 1
    count_frame = 0
    while vidcap.isOpened():
        success, image = vidcap.read()
        if count_frame == curent_frame and curent_frame < end_frame:
            filename_new = path_out + '\\' + filename + "_{:05d}.jpg".format(count_frame + 1)
            cv2.imwrite(filename_new, image)
            curent_frame += 1
        count_frame += 1
        if count_frame > end_frame:
            vidcap.release()
            print("FINISHED")
            break


def crop(url_in, url_out):
    # url_log = url_in + "\log.txt"
    url_log = os.path.join(url_in, "log.txt")
    txt_log = codecs.open(url_log, "+w", encoding="utf-8")
    list_duration = {}
    list_fps = {}

    for dirs, folders, filenames in os.walk(url_in):
        # read excel, get duration and fps
        for file in filenames:
            if file.endswith('.xlsx'):
                path_excel = os.path.join(dirs, file)
                rs_excel = get_list_duration_fps(path_excel)
                list_duration = rs_excel[0]
                list_fps = rs_excel[1]

        # get link, extract video
        for file in filenames:
            if file.endswith('.mov'):
                txt_log.write("- " + file + "\n")
                filename = file.rstrip('.mov')

                path_video = os.path.join(dirs, file)
                vidcap = cv2.VideoCapture(path_video)
                frame_rate = get_framerate(vidcap)

                path_out = os.path.join(url_out, filename)
                print(path_out)
                try:
                    os.mkdir(path_out)
                except OSError:
                    pass

                daration = list_duration[filename]
                fps_str = list_fps[filename]
                start_frame = get_start_frame(daration, frame_rate)
                end_frame = get_end_frame(daration, frame_rate)
                # jump_fps = get_jump_fps(fps_str, frame_rate)

                extract_vid(vidcap, frame_rate, start_frame, end_frame, fps_str, path_out, filename, txt_log)


if __name__ == "__main__":
    input_loc = r"D:\Sample\3_FPS"
    output_loc = r"D:\Sample\3_FPS"
    crop(input_loc, output_loc)
