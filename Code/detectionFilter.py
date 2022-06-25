import cv2
import numpy as np
import os
from mtcnn.mtcnn import MTCNN

#detectImg(img0) is for trial purpose only
'''def detectImg(img0):
    absolute_path = os.path.join(os.getcwd(), 'internalFiles', 'classifier.xml');
    faceCascade = cv2.CascadeClassifier(absolute_path)

    path = img0
    img = cv2.imread(path)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.04, 5)
    x, y, w, h = faces[0]
    imgW = img.shape[1]
    # print(imgW)

    divisions = imgW // 3
    # print(divisions)
    if x >= 0 and x < divisions:
        # print("l")
        return "left"
    elif x >= divisions and x < (2 * divisions):
        # print("c")
        return "center"
    elif x >= (2 * divisions) and x <= (3 * divisions):
        # print("r")
        return "right"
    else:
        # print("no case")
        return "center"     '''

def detectImgfirst():
    #absolute_path = os.path.join(os.getcwd(), 'internalFiles', 'classifier.xml');
    #faceCascade = cv2.CascadeClassifier(absolute_path)
    detector = MTCNN()

    path = os.path.join(os.getcwd(), 'internalFiles', 'splitFolder', '41.jpg');
    img = cv2.imread(path)

    #imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #faces = faceCascade.detectMultiScale(imgGray, 1.04, 5)
    faces = detector.detect_faces(img)
    
    x, y, w, h = faces[0]['box']
    imgW = img.shape[1]
    # print(x)
    # print(imgW)
    divisions = imgW // 3
    # print(divisions)
    if x >= 0 and x < divisions:
        # print("l")
        return "left"

    elif x >= (2 * divisions) and x <= (3 * divisions):
        # print("r")
        return "right"
    else:
        # print("no case")
        return "center"
