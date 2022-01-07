import cv2
import os

def split(videoName):
    absolute_path = os.path.join(os.getcwd(), 'input', videoName);
    vidcap = cv2.VideoCapture(absolute_path)
    success, image = vidcap.read()
    count = 0
    while success:
        split_path = os.path.join(os.getcwd(), 'internalFiles', 'splitFolder');
        cv2.imwrite(r"internalfiles\splitfolder\%d.jpg" % count,image)  # save frame as JPEG file
        success, image = vidcap.read()
        # print('Read a new frame: ', success)
        count += 1

