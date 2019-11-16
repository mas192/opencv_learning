# run script from terminal, pycharm freezes if run from here
# https://stackoverflow.com/questions/20539497/python-opencv-waitkey0-does-not-respond
# Cherif KAOUA response
# importing modules

import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype='uint8')
# drawing lines
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

# drawing rectangles
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

# drawing circles
# reinitialize a blank canvas
canvas = np.zeros((300, 300, 3),dtype='uint8')
# The height of the image can be found in canvas.shape[0]
# and the width in canvas.shape[1]

(centerX, centerY) = (int(canvas.shape[1]/2), int(canvas.shape[0]/2))
white = (255, 255, 255)

[cv2.circle(canvas, (centerX, centerY), r, white) for r in range(0, 175, 25)]
cv2.imshow('Canvas', canvas)
cv2.waitKey(0)

# random art

for i in range(0, 25):
    radius = np.random.randint(low=5, high=200)
    colour = np.random.randint(low=0, high=256, size=(3,)).tolist()
    pt = np.random.randint(low=0, high=300, size=(2,))
    cv2.circle(canvas, tuple(pt), radius, colour, -1)
cv2.imshow('Art', canvas)
cv2.waitKey(0)
