import cv2
import glob
import re
import os

def numericalSort(value):
    numbers = re.compile(r"(\d+)")
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

def merge():
    img_array = []
    numbers = re.compile(r"(\d+)")
    path = os.path.join(os.getcwd(), 'internalFiles', 'internalDewarped', '*.jpg');
    for filename in sorted(glob.glob(path) , key=numericalSort):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

    op_path = os.path.join(os.getcwd(), 'output','output.avi');
    out = cv2.VideoWriter(op_path, cv2.VideoWriter_fourcc(*'DIVX'), 24, size)
    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
