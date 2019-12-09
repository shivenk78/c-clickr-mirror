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
import time

# for linux
import pyscreenshot as imageGrab

# for windows and mac
# from PIL import ImageGrab

import imutils


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

def four_point_transform(image, pts):
    # obtain a consistent order of the points and unpack them
    # individually
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # compute the width of the new image, which will be the
    # maximum distance between bottom-right and bottom-left
    # x-coordiates or the top-right and top-left x-coordinates
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    # compute the height of the new image, which will be the
    # maximum distance between the top-right and bottom-right
    # y-coordinates or the top-left and bottom-left y-coordinates
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    # now that we have the dimensions of the new image, construct
    # the set of destination points to obtain a "birds eye view",
    # (i.e. top-down view) of the image, again specifying points
    # in the top-left, top-right, bottom-right, and bottom-left
    # order
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")

    # compute the perspective transform matrix and then apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    # return the warped image
    return warped


def order_points(pts):
    # initialzie a list of coordinates that will be ordered
    # such that the first entry in the list is the top-left,
    # the second entry is the top-right, the third is the
    # bottom-right, and the fourth is the bottom-left
    rect = np.zeros((4, 2), dtype="float32")

    # the top-left point will have the smallest sum, whereas
    # the bottom-right point will have the largest sum
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    # now, compute the difference between the points, the
    # top-right point will have the smallest difference,
    # whereas the bottom-left will have the largest difference
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    # return the ordered coordinates
    return rect


# capturing video through webcam
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
# cap.set(cv2.CAP_PROP_AUTO_WB, 0)

# list of distances found
patternList = []

# can give each distance a unique id???
idCount = 0

while (1):
    # img = cv2.imread('testImage.png', 1)
    image = imageGrab.grab()

    # cv2.imshow("raw", image)

    img = np.array(image)
    orig = img.copy()
    ratio = img.shape[0] / 500.0
    img = imutils.resize(img, height = 1000)




    # numpy be weird where blue and red are swapped
    red = img[:, :, 2].copy()
    blue = img[:, :, 0].copy()
    img[:, :, 0] = red
    img[:, :, 2] = blue

    img = cv2.bilateralFilter(img, 9, 75, 75)

    #img = cv2.imread('/home/maxwelllwang/c-clickr/testImage1.png', 1)
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
            #cv2.putText(img, "top color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

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
                    #cv2.putText(img, "bottom color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))
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
    crop_img = img.copy()
    for thing in patternList:
        #print("detected")
        # cv2.line(img, (thing.top.x, thing.top.y), (thing.bottom.x, thing.bottom.y), (0,0,0), 5)
        if thing.top.x < thing.bottom.x:
            dist = int((thing.bottom.x - thing.top.x) / 2)
            crop_img = img[abs(thing.top.y - dist):thing.top.y + dist, thing.top.x:thing.bottom.x]
        else:
            dist = int((thing.top.x - thing.bottom.x) / 2)
            crop_img = img[abs(thing.top.y - dist):thing.top.y + dist, thing.bottom.x:thing.top.x]

        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # # cv2.imshow("gray", gray)
        #
        # blur = cv2.GaussianBlur(gray, (5, 5), 0)
        # # cv2.imshow("blur", blur)
        #
        # thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
        #
        # (contours, ok1) = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 75, 200)
        cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

        maxArea = 0
        c = 0
        for i in cnts:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            area = cv2.contourArea(i)
            # if area > 1000 / 2:
            #     cv2.drawContours(img, contours, c, (0, 255, 0), 3)
            squares = 0
            if len(approx) == 4:
                squareContours = approx
                c += 1

                (x, y, w, h) = cv2.boundingRect(approx)
                #cv2.putText(img, "top color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))
                ar = w / float(h)
                print("found")
                # a square will have an aspect ratio that is approximately
                # equal to one, otherwise, the shape is a rectangle
                if ar >= 0.80 and ar <= 1.20:
                    squares += 1


                if area >= maxArea:
                    maxArea = area

                    biggestContour = squareContours

                    print(biggestContour)
                    cv2.drawContours(img, [biggestContour], -1, (0, 255, 0), 2)

                    warped = four_point_transform(orig, biggestContour.reshape(4, 2) * ratio)
                    #cv2.imshow("Warped", warped)
            #print(squares)

    cv2.imshow("cropped", imutils.resize(img, height=650))

    time.sleep(.5)

    # cv2.imshow("cropped", thresh)
    # print("(" + str(thing.top.x) + "," + str(thing.top.y) + ")\t" + "(" + str(thing.bottom.x) + "," + str(thing.bottom.y) + ")\t" + "Distance:" + str(thing.distance))

    # cv2.imshow("Redcolour",red)
    # cv2.imshow("Color Tracking", img)
    img = cv2.flip(img, 1)
    # cv2.imshow("red",res)qqq
    if cv2.waitKey(10) & 0xFF == ord('q'):
        # cap.release()
        cv2.destroyAllWindows()
        break


