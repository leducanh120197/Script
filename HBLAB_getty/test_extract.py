import cv2
import time
import os
import codecs

list_var = [12, 25]

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



    count_frame = 0
    curent_frame = 12.5
    while vidcap.isOpened():
        success, image = vidcap.read()
        # print(success)
        # creat image name
        if count_frame == int(curent_frame) and curent_frame < 301:
            filename_new = url_out + '\\' + filename + "_{:05d}.jpg".format(count_frame)
            print(filename_new)

            # filename_new = 'frame%d.jpg' % count_frame
            # print(filename_new)

            cv2.imwrite(filename_new, image)

            # success, image = vidcap.read()
            curent_frame += 12.5
        count_frame += 1
        if curent_frame > 300:
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


if __name__=="__main__":
    input_loc = r'D:\abc'
    output_loc = r'D:\abc'
    crop(input_loc, output_loc)

