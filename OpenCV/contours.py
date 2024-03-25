'''
Contour is the outline or shape of something. 
In image processing, contours are used to detect the shape of an object.
These are different from edges. Edges are the points where the image brightness changes sharply.
'''

import cv2 as cv
import numpy as np


img = cv.imread('./assets/Photos/cats.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

blurred = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blurred', blurred)

# Canny Edge Detection
canny = cv.Canny(blurred, 125, 175)
cv.imshow('Canny Edges', canny)

ret, thres = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresholded', thres)

# Contours
# cv.findContours(image, mode, method)
# mode: RETR_LIST, RETR_EXTERNAL, RETR_TREE
# method: CHAIN_APPROX_NONE, CHAIN_APPROX_SIMPLE
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

# Draw contours
# cv.drawContours(image, contours, contour_index, color, thickness)
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
cv.destroyAllWindows()