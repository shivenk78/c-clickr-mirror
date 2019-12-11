import cv2
import numpy as np
import pyscreenshot as ImageGrab
import math
import time
import imutils


while(1):
    image = ImageGrab.grab()

    # cv2.imshow("raw", image)
    img = np.array(image)

    # numpy be weird where blue and red are swapped
    red = img[:, :, 2].copy()
    blue = img[:, :, 0].copy()
    img[:, :, 0] = red
    img[:, :, 2] = blue

    img = cv2.bilateralFilter(img, 9, 75, 75)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

    # find contours in the thresholded image and initialize the
    # shape detector
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    squares = 0
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)

        if len(approx) == 4:
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)

            # a square will have an aspect ratio that is approximately
            # equal to one, otherwise, the shape is a rectangle
            if ar >= 0.95 and ar <= 1.05:
                squares = squares + 1
    cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
    cv2.imshow('ree', img)

    print(squares)
    



