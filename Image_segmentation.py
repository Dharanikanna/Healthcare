import pydicom as dicom
import numpy as np
import cv2
import matplotlib.pyplot as plt

img=dicom.dcmread('image-00002.dcm')

#show header data
print(img)

testarray = img.pixel_array

frames=img.NumberOfFrames
width= img.Rows
height=img.Columns
shape=testarray.shape

print(frames,width,height,shape)