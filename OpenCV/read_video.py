import cv2 as cv

# Read video
# 0 is the default camera
# capture = cv.VideoCapture(0)

# Read video from file
capture = cv.VideoCapture('./assets/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    
    cv.imshow('Video', frame)

    # If the letter 'd' is pressed, break the loop
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()

cv.destroyAllWindows()