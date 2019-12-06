''' 
- Currently gives all distances where the magenta and cyan are at a large enough area so it should not track background noise
- Will give ALL distances between including distances between the magenta and cyan of two completely different patters. 
- for some reason I refer to magenta as red and cyan as blue for most of this code
- VSCode shows cv2 underlined in red but it works so...
'''
# importing modules

import cv2
import numpy as np
import math
from PIL import ImageGrab
import time

# create class to store pattern objects
class pattern:
    def __init__(self, id, magenta, cyan, distance):
        self.id = id
        self.top = magenta
        self.bottom = cyan
        self.distance = distance


class coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# capturing video through webcam
# cap=cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
# cap.set(cv2.CAP_PROP_AUTO_WB, 0)

# list of distances found
patternList = []

# can give each distance a unique id???
idCount = 0

while (1):

    # _, img = cap.read()

    #img = cv2.imread('testImage.png', 1)
    image = ImageGrab.grab()
    img = np.array(image)

    # numpy be weird where blue and red are swapped
    red = img[:, :, 2].copy()
    blue = img[:, :, 0].copy()
    img[:, :, 0] = red
    img[:, :, 2] = blue

    # list is cleared for each run through
    patternList = []

    # converting frame(img i.e BGR) to HSV (hue-saturation-value)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # definig the range of magenta color
    red_lower = np.array([147, 115, 150], np.uint8)
    red_upper = np.array([150, 255, 255], np.uint8)

    # defining the Range of cyan color
    blue_lower = np.array([87, 115, 150], np.uint8)
    blue_upper = np.array([93, 255, 255], np.uint8)

    # finding the range of magenta,cyan and other colors in the image
    red = cv2.inRange(hsv, red_lower, red_upper)
    blue = cv2.inRange(hsv, blue_lower, blue_upper)

    # Morphological transformation, Dilation
    kernal = np.ones((5, 5), "uint8")

    red = cv2.dilate(red, kernal)
    res = cv2.bitwise_and(img, img, mask=red)

    blue = cv2.dilate(blue, kernal)
    res1 = cv2.bitwise_and(img, img, mask=blue)

    # variables to store the coordinates
    redX = 0
    redY = 0
    blueX = 0
    blueY = 0

    # Tracking the Red Color
    (contours, hierarchy) = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        redArea = cv2.contourArea(contour)
        if (redArea > 400):
            x, y, w, h = cv2.boundingRect(contour)

            # draws rectangle and label
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "top color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

            # finds centroid and draws it
            M = cv2.moments(contour)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            cv2.putText(img, "(" + str(center[0]) + "," + str(center[1]) + ")", (center[0] + 10, center[1] + 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
            redX = center[0]
            redY = center[1]
            cv2.circle(img, center, 2, (0, 0, 0))

            # for each Red contour, loop through blue and compare distance (tested other methods and this works best)
            (contoursBlue, hierarchyBlue) = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            for pic, contour in enumerate(contoursBlue):
                blueArea = cv2.contourArea(contour)
                if (abs(blueArea) > 400):
                    x, y, w, h = cv2.boundingRect(contour)
                    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    cv2.putText(img, "bottom color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))
                    M = cv2.moments(contour)
                    centerBlue = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                    cv2.putText(img, "(" + str(center[0]) + "," + str(center[1]) + ")",
                                (center[0] + 10, center[1] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 0, 0), 1)
                    blueX = centerBlue[0]
                    blueY = centerBlue[1]
                    cv2.circle(img, centerBlue, 2, (0, 0, 0))

                    # if either coordinate is (0,0) that means it is not found and should not be appended to the list
                    if not (redX == 0 and redY == 0) and not (blueX == 0 and blueY == 0):
                        distance = math.sqrt(((redX - blueX) ** 2) + ((redX - blueX) ** 2))

                        # create object and append to the list
                        # first create two coordinate objects and then add that to the pattern object
                        magenta = coordinates(redX, redY)
                        cyan = coordinates(blueX, blueY)
                        p1 = pattern(idCount, magenta, cyan, distance)
                        patternList.append(p1)
                        idCount = idCount + 1
    # show each distance calculated
    for thing in patternList:
        cv2.line(img, (thing.top.x, thing.top.y), (thing.bottom.x, thing.bottom.y), (0, 0, 0), 5)
        # print("(" + str(thing.top.x) + "," + str(thing.top.y) + ")\t" + "(" + str(thing.bottom.x) + "," + str(thing.bottom.y) + ")\t" + "Distance:" + str(thing.distance))

    # cv2.imshow("Redcolour",red)
    cv2.imshow("Color Tracking", img)
    img = cv2.flip(img, 1)
    time.sleep(5)
    # cv2.imshow("red",res)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        #cap.release()
        cv2.destroyAllWindows()
        break

