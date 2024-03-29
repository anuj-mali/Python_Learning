import cv2 as cv

# BGR image
img = cv.imread('./assets/Photos/park.jpg')
cv.imshow('Original', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur image
blurred = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blurred', blurred)

# Edge cascade 
# show the edges of the image
canny = cv.Canny(blurred, 125, 175)
# cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (3,3), iterations=1)
# cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
# cv.imshow('Eroded', eroded)

# Resize 
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
cv.destroyAllWindows()