import argparse
import cv2

ap = argparse.ArgumentParser()

#path to image
ap.add_argument('-i', '--image', required=True,
                help='Path to image')
#path to save processed image

ap.add_argument('-o','--image', required=True,
                help='Saved image path')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
print(f'Width of image is {image.shape[1]} pixels')
print(f'Height of image is {image.shape[0]} pixels ')
print(f'The # of channels in image is {image.shape[2]}')

cv2.imshow('Original', image)
cv2.waitKey(0)


