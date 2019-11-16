import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True,
                help='Path to the image')
args = vars(ap.parse_args())
image = cv2.imread(args['image'])
cv2.imshow('Original', image)
cv2.waitKey(0)
(b, g, r) = image[0, 0]
print(f'Pixel at (0, 0) - Red: %d, Green: %d, Blue %d' % (r, g, b))
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print(f'Modified pixel at (0, 0) - Red: %d, Green: %d, Blue %d' % (r, g, b))

# grabing a 100 by 100 at top left corner
left_corner = image[0:100, 0:100]
cv2.imshow('Left Corner', left_corner)
cv2.waitKey(0)

image[0:100, 0:100] = (0, 255, 0)
cv2.imshow('Left corner modified', image)
cv2.waitKey(0)