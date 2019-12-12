import cv2 as cv
import numpy as np

img = cv.imread("/home/maxwelllwang/c-clickr/opencv_testing/camShiftTest.jpg")
roi = img[124: 357, 86: 231]
x = 124
y = 86
width = 357- x
height = 231 - y
cv.imshow('pic', roi)
hsv_roi = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
roi_hist = cv.calcHist([hsv_roi], [0], None, [180], [0, 180])
cap = cv.VideoCapture(0)
term_criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)
while True:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    mask = cv.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
    ret, track_window = cv.CamShift(mask, (x, y, width, height), term_criteria)
    pts = cv.boxPoints(ret)
    pts = np.int0(pts)
    cv.polylines(frame, [pts], True, (255, 0, 0), 2)
    cv.imshow("mask", mask)
    cv.imshow("Frame", frame)

    # coutours
    blurred_frame = cv.GaussianBlur(frame, (5, 5), 0)
    hsv = cv.cvtColor(blurred_frame, cv.COLOR_BGR2HSV)

    lower_blue = np.array([38, 86, 0])
    upper_blue = np.array([121, 255, 255])
    mask1 = cv.inRange(hsv, lower_blue, upper_blue)

    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    for contour in contours:
        area = cv.contourArea(contour)
        if area > 1000:
            cv.drawContours(frame, contour, -1, (0, 255, 0), 3)
            

    cv.imshow("Frame", frame)
    cv.imshow("Mask", mask1)

    key = cv.waitKey(1)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()