import cv2 as cv

# Read image
img = cv.imread('./assets/Photos/cat_large.jpg')
cv.imshow('Cat', img)

# Waits the specified milliseconds for any keyboard event
# 0 means wait indefinitely
cv.waitKey(0)

# Closes all windows
cv.destroyAllWindows()
