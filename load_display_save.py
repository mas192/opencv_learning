import argparse
import cv2
import os
import numpy as np
from imutils.object_detection import non_max_suppression
import pytesseract
'''https://www.pyimagesearch.com/2018/09/17/
opencv-ocr-and-text-recognition-with-tesseract/'''
ap = argparse.ArgumentParser()

#path to image
ap.add_argument('-i', '--image', required=True,
                help='Path to image')
#path to save processed image

'''ap.add_argument('-o','--output', required=True,
                help='Saved image path')
os.chdir()
cv2.imwrite('Processed',)'''
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
print(f'Width of image is {image.shape[1]} pixels')
print(f'Height of image is {image.shape[0]} pixels ')
print(f'The # of channels in image is {image.shape[2]}')

cv2.imshow('Original', image)
cv2.waitKey(0)


