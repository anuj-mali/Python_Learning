import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    '''
    Function to rescale the frame of the video
    Works for images, video and live video
    '''
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    '''
    Function to change the resolution of the video
    Works for live video only
    '''
    capture.set(3, width)
    capture.set(4, height)

# capture = cv.VideoCapture('./assets/Videos/dog.mp4')
# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame)
#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    changeRes(frame.shape[1], frame.shape[0])
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()