import cv2 as cv 
import numpy as np

img = cv.imread('./assets/Photos/park.jpg')
cv.imshow('Park', img)

# Translation
def translate(img, x_shift, y_shift):
    transMat = np.float32([[1,0,x_shift],[0,1,y_shift]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# translated = translate(img, 100, 100)
# cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    height,width = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img, 45)
# cv.imshow('Rotated', rotated)

# Resizing
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# cv.imshow('Resized', resized)

# Reflection
# flip code 0: vertical, 1: horizontal, -1: both
# flip = cv.flip(img, -1)
# cv.imshow('Flipped', flip)

# Cropping
cropped = img[200:400, 300:600]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
cv.destroyAllWindows()