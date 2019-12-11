# import the necessary packages
import argparse
import imutils
import cv2
from imutils.video import VideoStream
import numpy as np
import time

# capture frames from a camera
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

# loop runs if capturing has been initialized
while(1):
    # reads frames from a camera
    res, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])

    time.sleep(2.0)

    mask = cv2.inRange(hsv, lower_red, upper_red)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 400:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
        if len(approx) == 3:
            cv2.putText(frame, "Triangle", (x, y), font, 1, (0, 0, 0))
        elif len(approx) == 4:
            cv2.putText(frame, "Rectangle", (x, y), font, 1, (0, 0, 0))
        elif 10 < len(approx) < 20:
            cv2.putText(frame, "Circle", (x, y), font, 1, (0, 0, 0))

    # finds edges in the input image image and
    # marks them in the output map edges
    edges = cv2.Canny(frame,100,200)

    # Display edges in a frame
    cv2.imshow('Frame',frame)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    '''
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # convert the resized image to grayscale, blur it slightly,
    # and threshold it
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

    # find contours in the thresholded image and initialize the
    # shape detector
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
    	cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    sd = ShapeDetector()
    # loop over the contours
    for c in cnts:
    	# compute the center of the contour, then detect the name of the
    	# shape using only the contour
    	M = cv2.moments(c)
    	cX = int((M["m10"] / M["m00"]) * ratio)
    	cY = int((M["m01"] / M["m00"]) * ratio)
    	shape = sd.detect(c)

    	# multiply the contour (x, y)-coordinates by the resize ratio,
    	# then draw the contours and the name of the shape on the image
    	c = c.astype("float")
    	c *= ratio
    	c = c.astype("int")
    	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    	cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
    		0.5, (255, 255, 255), 2)

    # if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

# if we are not using a video file, stop the camera video stream
if not args.get("video", False):
    vs.stop()

# otherwise, release the camera
else:
    vs.release()
'''

# close all windows
cv2.destroyAllWindows()
