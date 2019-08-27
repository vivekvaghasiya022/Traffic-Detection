import cv2 as cv
import numpy as np

video = cv.VideoCapture("vid3.mp4")

while True:
    check, frame = video.read()
    frame = cv.resize(frame, (540, 380))
    cv.imshow("Original", frame)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        cv.imwrite("op3.png",frame)
        break


cv.destroyAllWindows()
video.release()
