import cv2 as cv
import numpy as np


blank = np.zeros((500, 500, 3), dtype='uint8')


# Paint the image
blank[:] = 0, 255, 0

# Paint certain area
blank[200:300, 300:400] = 0, 0, 255

# Draw a rectangle
# image, start_point, end_point, color, thickness
#  -1 for fill the rectangle
cv.rectangle(blank, (250,0), (500,250), (255, 255, 0), thickness=-1)
cv.rectangle(blank, (0,0), (250,250), (255, 0, 0), thickness=2)

# Draw a circle
# image, center, radius, color, thickness
cv.circle(blank, (250,250), 30, (0,0,255), thickness=3)

# Draw a line
# image, start_point, end_point, color, thickness
cv.line(blank, (0,0), (500,500), (0, 255, 255), thickness=3)

# Write text
# image, text, origin, font, scale, color, thickness
cv.putText(img=blank, text='Anuj', org=(260,240), fontFace=cv.FONT_HERSHEY_TRIPLEX, fontScale=1.0, color=(0,255,255), thickness=2)

cv.imshow('Blank', blank)
cv.waitKey(0)
cv.destroyAllWindows()