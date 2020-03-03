import os
import codecs
import time
import cv2
import xlrd
import re


def get_start_frame(var):
    var = int(var[2:4])
    var = var*25
    return var


def get_end_frame(var):
    var = int(var[9:11])
    # print( + str(var))
    var = var*25
    return var


def get_fps(var):
    fps = int(var[:1])
    if fps == 2:
        return 12.5
    if fps == 1:
        return 25


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


def extract_vid(url_in, url_out, filename, txt_log, list_duration, list_fps):
    # Log the start time


    vidcap = cv2.VideoCapture(url_in)
    video_fps = vidcap.get(cv2.CAP_PROP_FPS)
    if video_fps == 25:
        time_start = time.time()

        #create url output
        try:
            os.mkdir(url_out)
        except OSError:
            pass
        video_length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
        video_msc = int(vidcap.get(cv2.CAP_PROP_POS_MSEC))

        # write log
        print("Duration in miliseconds", video_msc)
        print("Number of frames: ", video_length)
        print("FPS : ", video_fps)
        txt_log.write("\tDuration in miliseconds: {} \n".format(video_msc))
        txt_log.write("\tNumber of frames: {} \n".format(video_length))
        txt_log.write("\tFPS : {} \n".format(video_fps))

        count_frame = 0
        daration = list_duration[filename]
        fps_to_frame = get_fps(list_fps[filename])
        curent_frame = get_start_frame(daration)
        end_frame = get_end_frame(daration)

        while vidcap.isOpened():
            success, image = vidcap.read()

            # creat image name
            if count_frame == int(curent_frame) and curent_frame < end_frame:
                filename_new = url_out + '\\' + filename + "_{:05d}.jpg".format(count_frame+1)
                cv2.imwrite(filename_new, image)
                curent_frame += fps_to_frame
            count_frame += 1
            if count_frame > end_frame:
                # Release the feed
                vidcap.release()

                # Log the end time again
                time_end = time.time()

                # Write log
                print ("Done extracting frames: %d frames extracted" % count_frame)
                print ("It took %d seconds forconversion." % (time_end-time_start))
                txt_log.write("\tDone extracting frames: {:d}\n".format(count_frame))
                txt_log.write("\tIt took {:f} seconds forconversion.\n".format(time_end-time_start))
                break


def crop(url_in, url_out):
    url_log = url_in + "\log.txt"
    txt_log = codecs.open(url_log, "+w", encoding="utf-8")
    list_duration = {}
    list_fps = {}

    for dirs, folders, filenames in os.walk(url_in):
        for file in filenames:
            if file.endswith('.xlsx'):
                path_excel = os.path.join(dirs, file)
                rs_excel = get_list_duration_fps(path_excel)
                list_duration = rs_excel[0]
                list_fps = rs_excel[1]

        for file in filenames:
            if file.endswith('.mov'):
                txt_log.write("- " + file + "\n")
                filename = file.rstrip('.mov')
                path_in = os.path.join(dirs, file)
                path_out = os.path.join(url_out, filename)
                extract_vid(path_in, path_out, filename, txt_log, list_duration, list_fps)


if __name__=="__main__":
    input_loc = r'D:\HBLAB_getty\video'
    output_loc = r'D:\HBLAB_getty\video'
    crop(input_loc, output_loc)
