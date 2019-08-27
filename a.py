import cv2 as cv
import numpy as np
video = cv.VideoCapture("a.mp4")
car_cascade = cv.CascadeClassifier('cars.xml')
while True:
    check, frame = video.read()
    frame = cv.resize(frame, (640,480))
    copy = cv.resize(frame,(640,480))
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.1,3)
    for(x,y,w,h) in cars:
        cv.rectangle(copy, (x, y), (x+w, y+h), (255, 255, 255),-1)
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255),-1)
        

    rows = copy.shape[0]
    cols = copy.shape[1]
    for i in range(rows):
        for j  in range(cols):
            if np.array_equal(copy[i,j],[255,255,255]):
                pass
            else:
                copy[i,j] = [0,0,0]

    cv.imshow("frame",frame)
    cv.imshow("copy",copy)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
video.release()