import cv2 as cv
import numpy as np

video = cv.VideoCapture("a.mp4")

# for vid "a.mp4"
lower_gray = np.array([110, 4, 103])
upper_gray = np.array([130, 24, 183])

blank_frame = cv.imread("c.png")

# def giveMePercentageOf(rg, resolution):
#     count = 0
#     rows = rg.shape[0]
#     cols = rg.shape[1]
#     for i in range(rows):
#         for j in range(cols):
#             if np.array_equal(rg[i, j], [0, 0, 0]):
#                 count += 1
#     res = (100.0 * count) / resolution
#     # print(avg - rg)
#     # res = str(rg.mean())[0:5]
#     return str(100 - res)[0:5]

pts = np.array([[208, 135], [74, 372], [457, 373], [354,133]], np.int32)
# pts = pts.reshape((-1,1,2))

while video.get(cv.CAP_PROP_POS_FRAMES) != video.get(cv.CAP_PROP_FRAME_COUNT):
    check, frame = video.read()
    frame = cv.resize(frame, (540, 380))
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)


    # # # # # # # # # # # # # # # # # SJ24

    # img = np.copy(frame)
    # contours = [pts]
    # # print(contours, contours[0].shape, type([pts]))
    # mask = np.zeros_like(img)
    # cv.drawContours(mask, contours, -1, (0, 255, 0), 3)
    # out = np.zeros_like(img)

    # out[mask == 255] = img[img == (0, 255, 0)]

    # cv.imshow('Output222', out)

    # # # # # # # # # # # # # # # # # SJ24

    
    #

    # imgray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # ret, thresh = cv.threshold(imgray, 127, 255, 0)
    # contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    # print(contours[0].shape)

    #

    mask = cv.inRange(hsv, lower_gray, upper_gray)

    # _, contours = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
    # img = np.copy(frame)
    # cv.drawContours(img, contours, -1, (0, 255, 0), 3)
    # cv.imshow("Img", img)

    res = cv.bitwise_and(frame, frame, mask=mask)


    median = cv.medianBlur(res, 7)

    region = median[179:375, 188:438]
    s1 = (region < 128).sum()
    s0 = (region > 127).sum()
    p = (s1 * 100) / (s0 + s1)
    
    cv.rectangle(median, (188, 179), (438, 375), (0, 255, 0), 3)
    # cv.polylines(frame,[pts],True, (0,255,0),2)

    # per = "Detected Road: " + giveMePercentageOf(region, region.shape[0] * region.shape[1]) + "%"
    per = "Traffic Level: " + str(round(p, 2)) + "%"

    cv.putText(median, per, (10, 30), cv.FONT_HERSHEY_DUPLEX,1, (0, 255, 0), 1, cv.LINE_AA)

    cv.imshow("Original", frame)
    cv.imshow("mask",mask)
    cv.imshow("res",res)
    cv.imshow("Output", median)
    cv.imshow("reg",region)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        cv.imwrite("ss.png",frame)
        break

cv.destroyAllWindows()
video.release()