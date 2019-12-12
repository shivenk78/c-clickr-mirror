import cv2
import numpy as np
import math
import pyscreenshot as imageGrab
import time

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6 * 8, 3), np.float32)
objp[:, :2] = np.mgrid[0:8, 0:6].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = []  # 3d points in real world space
imgpoints = []  # 2d points in image plane.

# Make a list of calibration images


# Step through the list and search for chessboard corners
while (1):

    image = imageGrab.grab()

    # cv2.imshow("raw", image)
    img = np.array(image)

    # numpy be weird where blue and red are swapped
    red = img[:, :, 2].copy()
    blue = img[:, :, 0].copy()
    img[:, :, 0] = red
    img[:, :, 2] = blue

    #img = cv2.imread('/home/maxwelllwang/c-clickr/testImage.png', -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (5, 5), None)
    cv2.imshow('img', img)
    # If found, add object points, image points
    if ret == True:
        objpoints.append(objp)
        imgpoints.append(corners)

        # Draw and display the corners
        cv2.drawChessboardCorners(img, (5, 5), corners, ret)
        # write_name = 'corners_found'+str(idx)+'.jpg'
        # cv2.imwrite(write_name, img)
        cv2.imshow('img', img)
        cv2.waitKey(500)

    objpoints.append(objp)
    imgpoints.append(corners)

    # Draw and display the corners
    cv2.drawChessboardCorners(img, (5, 5), corners, ret)
    # write_name = 'corners_found'+str(idx)+'.jpg'
    # cv2.imwrite(write_name, img)
    cv2.imshow('img', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        # cap.release()
        cv2.destroyAllWindows()
        break
