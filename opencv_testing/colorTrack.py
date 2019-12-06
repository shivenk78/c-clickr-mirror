# importing modules

import cv2
import numpy as np

# capturing video through webcam
cap = cv2.VideoCapture(0)

magentaColor = np.uint8([[[255, 0, 255]]])
hsv_green = cv2.cvtColor(magentaColor,cv2.COLOR_BGR2HSV)
print(hsv_green)

def nothing(x):
    print(x)


# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('adjust range')

cv2.createTrackbar('Magenta Range', 'adjust range', 0, 255, nothing)
cv2.createTrackbar('red up', 'adjust range', 0, 255, nothing)
cv2.createTrackbar('red down', 'adjust range', 0, 255, nothing)
cv2.createTrackbar('area', 'adjust range', 200, 5000, nothing)
cv2.createTrackbar('Color Range', 'adjust range', 0, 100, nothing)
#
# switch = '0 : OFF\n 1 : ON'
# cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while (1):
    _, img = cap.read()

    # converting frame(img i.e BGR) to HSV (hue-saturation-value)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    magenta_range = cv2.getTrackbarPos('Magenta Range', 'adjust range')
    redUp = cv2.getTrackbarPos('red up', 'adjust range')
    redDown = cv2.getTrackbarPos('red down', 'adjust range')
    areaSize = cv2.getTrackbarPos('area', 'adjust range')
    colorRange = cv2.getTrackbarPos('Color Range', 'adjust range')

    #adjustable ranges
    #definig the range of red color
    red_lower = np.array([155 - colorRange, 87, 111], np.uint8)
    red_upper = np.array([155 + colorRange, 255, 255], np.uint8)

    # defining the Range of Blue color
    blue_lower = np.array([105, 115, 150], np.uint8)
    blue_upper = np.array([105 + (colorRange / 2), 255, 255], np.uint8)

    # defining the Range of yellow color
    yellow_lower = np.array([30 - colorRange, 60, 200], np.uint8)
    yellow_upper = np.array([30 + colorRange, 255, 255], np.uint8)

    # defining the Range of green color
    green_lower = np.array([65 - colorRange, 100, 50], np.uint8)
    green_upper = np.array([65 + colorRange, 255, 255], np.uint8)

    # defining the Range of magenta color
    magenta_lower = np.array([150 - colorRange, 0, 220], np.uint8)
    magenta_upper = np.array([150 + colorRange, 40, 255], np.uint8)

    #not adjustable ranges

    # red_lower = np.array([136, 87, 111], np.uint8)
    # red_upper = np.array([180, 255, 255], np.uint8)
    #
    # # defining the Range of Blue color
    # blue_lower = np.array([99, 115, 150], np.uint8)
    # blue_upper = np.array([110, 255, 255], np.uint8)
    #
    # # defining the Range of yellow color
    # yellow_lower = np.array([22, 60, 200], np.uint8)
    # yellow_upper = np.array([50, 255, 255], np.uint8)
    #
    # # defining the Range of green color
    # green_lower = np.array([50, 100, 50], np.uint8)
    # green_upper = np.array([80, 255, 255], np.uint8)
    #
    # # defining the Range of magenta color
    # magenta_lower = np.array([140, 0, 220], np.uint8)
    # magenta_upper = np.array([160, 40, 255], np.uint8)

    # finding the range of red,blue and yellow color in the image
    red = cv2.inRange(hsv, red_lower, red_upper)
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
    magenta = cv2.inRange(hsv, magenta_lower, magenta_upper)
    green = cv2.inRange(hsv, green_lower, green_upper)

    # Morphological transformation, Dilation
    kernal = np.ones((5, 5), "uint8")

    red = cv2.dilate(red, kernal)
    res = cv2.bitwise_and(img, img, mask=red)

    blue = cv2.dilate(blue, kernal)
    res1 = cv2.bitwise_and(img, img, mask=blue)

    yellow = cv2.dilate(yellow, kernal)
    res2 = cv2.bitwise_and(img, img, mask=yellow)

    magenta = cv2.dilate(magenta, kernal)
    res2 = cv2.bitwise_and(img, img, mask=magenta)

    green = cv2.dilate(green, kernal)
    res2 = cv2.bitwise_and(img, img, mask=green)

    # Tracking the Red Color
    (contours, hierarchy) = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > areaSize):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "RED color " + str(area), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))


    (contours, hierarchy) = cv2.findContours(magenta, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #tracking bottem of phone
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > areaSize):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, "Bottom of Phone " + str(area), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255))

    # Tracking the Blue Color
    (contours, hierarchy) = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > areaSize):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "Blue color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))

    # Tracking green
    (contours, hierarchy) = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > areaSize):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "green " + str(area), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

    # Tracking yellow
    (contours, hierarchy) = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "yellow " + str(area), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))


    # cv2.imshow("Redcolour",red)
    cv2.imshow("Color Tracking", img)
    # cv2.imshow("red",res)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break