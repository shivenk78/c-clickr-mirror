# OpenCV program to perform Edge detection in real time
# import libraries of python OpenCV
# where its functionality resides
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64,
	help="max buffer size")
args = vars(ap.parse_args())


# capture frames from a camera
cap = cv2.VideoCapture(0)


# loop runs if capturing has been initialized
while(1):

    # reads frames from a camera
    ret, frame = cap.read()

    # converting BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv2 = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # define the range of pink that is on the bottom of the pattern
    lower_pink = np.array([156, 74, 76])
    upper_pink = np.array([166, 255, 255])

    pts = deque(maxlen=args["buffer"])

    # if a video path was not supplied, grab the reference
    # to the webcam
    if not args.get("video", False):
    	vs = VideoStream(src=0).start()

    # otherwise, grab a reference to the video file
    else:
    	vs = cv2.VideoCapture(args["video"])

    # allow the camera or video file to warm up
    time.sleep(2.0)

    # create a red and pink HSV colour boundary and
    # threshold HSV image
    colorMask = cv2.inRange(hsv2, lower_pink, upper_pink)
    colormask = cv2.erode(colorMask, None, iterations=2)
    colorMask = cv2.dilate(colorMask, None, iterations=2)

    #Segmenting the pink out of the frame using bitwise and with the inverted mask
    colorRes = cv2.bitwise_and(frame,frame,mask=colorMask)

    # find contours in the mask and initialize the current
	# (x, y) center of the ball
    cnts = cv2.findContours(colorMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    center = None

    # only proceed if at least one contour was found
    if len(cnts) > 0:
        # find the largest contour in the mask, then use
        # it to compute the minimum enclosing circle and
        # centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # only proceed if the radius meets a minimum size
        if radius > 10:
            # draw the circle and centroid on the frame,
            # then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            # loop over the set of tracked points
    # update the points queue
    pts.appendleft(center)

    for i in range(1, len(pts)):
    	# if either of the tracked points are None, ignore
    	# them
        if pts[i - 1] is None or pts[i] is None:
            continue

    	# otherwise, compute the thickness of the line and
    	# draw the connecting lines
        thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
        cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

	# show the frame to our screen
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

	# if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

# if we are not using a video file, stop the camera video stream
if not args.get("video", False):
	vs.stop()

# otherwise, release the camera
else:
	vs.release()

# close all windows
cv2.destroyAllWindows()

'''
    # finds edges in the input image image and
    # marks them in the output map edges
    edges = cv2.Canny(frame,100,200)

    # Display edges in a frame
    cv2.imshow('Edges',edges)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
'''


# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
