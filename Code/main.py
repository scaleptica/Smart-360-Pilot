import os
import cv2
import detectionFilter
import splitPano
import mergeDewarped
import getViewDewarped
import glob
import numpy as np

#Relative File Paths for reference
panoVid = "surfing.mp4"     #This is the name of the video file

# internal program directories
splitFramesDir = "\interalFiles\splitFolder"
dwDir = "\internalFiles\internalDewarped"
outputDir = "output"

#processes
print("Process started")
splitPano.split(panoVid)
print("1. Splitting done")
getViewDewarped.getViewDewarped()
print("2. Dewarping done")
mergeDewarped.merge()
print("3. Merging done")
print("4. Output saved in output folder")

# Flushing any previous files from before
absolute_path = os.path.join(os.getcwd(), 'internalFiles', 'splitFolder');
filelist = glob.glob(os.path.join(absolute_path, "*"))
for f in filelist:
    os.remove(f)

absolute_path = os.path.join(os.getcwd(), 'internalFiles', 'internalDewarped');
filelist = glob.glob(os.path.join(absolute_path, "*"))
for f in filelist:
    os.remove(f)