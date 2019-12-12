#DetectColor - used to divide a Quadrilateral into sixteenths and find the average color
#            - (turning given Quadrilateral into array of colors)

from Quadrilateral import Quadrilateral
from ConvertToUIN import *
import numpy as np
import cv2
import math
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#array storing UINs
uin_array = []

#takes a Quadrilateral and returns sixteen rectangles to find the average color of
def sixteenthArray(root):
    topLeftQuarter = root.findQuarterQuad(1)
    topRightQuarter = root.findQuarterQuad(2)
    botLeftQuarter = root.findQuarterQuad(3)
    botRightQuarter = root.findQuarterQuad(4)

    quarterArray = [topLeftQuarter, topRightQuarter, botLeftQuarter, botRightQuarter]
    colorRects = []
    for quarter in quarterArray:
        for i in range(1, 5):
            sixteenth = quarter.findQuarterQuad(i)
            colorRects.append(sixteenth.findRectFit())
    return colorRects

#gets the average color in a given rectangle
def array_average_color(array, image):
    color_array = []
    for rectangle in array:
        color_array.append(rectangle.getAverageColor(image))
    return color_array

#since the array given by sixteenthArray will be out of order,
#this will put it in the correct to be decoded
def rearrange(array):
    for half in range(2):
        switch = half * 8
        temp1 = array[switch + 2]
        temp2 = array[switch + 3]
        array[switch + 2] = array[switch + 4]
        array[switch + 3] = array[switch + 5]
        array[switch + 4] = temp1
        array[switch + 5] = temp2
    return array

def color_balance(img):
    magenta_box = Quadrilateral((0,0), (len(img[0]),0), (0,(7/32) * len(img)), (len(img[0]),(7/32) * len(img)))
    avg_color = (magenta_box.findRectFit()).getAverageColor(img)
    print(avg_color)
    return (255 - avg_color[0], avg_color[1], 255 - avg_color[2])

"""Apply Simplest Color Balance algorithm
Reimplemented based on https://gist.github.com/DavidYKay/9dad6c4ab0d8d7dbf3dc"""
def simplest_cb(img, percent):
    out_channels = []
    channels = cv2.split(img)
    totalstop = channels[0].shape[0] * channels[0].shape[1] * percent / 200.0
    for channel in channels:
        bc = np.bincount(channel.ravel(), minlength=256)
        lv = np.searchsorted(np.cumsum(bc), totalstop)
        hv = 255-np.searchsorted(np.cumsum(bc[::-1]), totalstop)
        out_channels.append(cv2.LUT(channel, np.array(tuple(0 if i < lv else 255 if i > hv else round((i-lv)/(hv-lv)*255) for i in np.arange(0, 256)), dtype="uint8")))
    return cv2.merge(out_channels)

def distance(pt1, pt2):
    return pt2 - pt1

# converts base 10 UIN to base 4 code
def uin_to_code(new_uin_str):
    code = 0
    uin = int(new_uin_str)
    multiplier = 1

    while uin != 0:
        code += (uin % 4) * multiplier
        uin = int(uin / 4)
        multiplier *= 10

    code_str = str(code)
    while len(code_str) < 16:
        code_str = "0" + code_str

    return code_str


def master_runner(image, topLeft, topRight, botRight, botLeft):
    uncropped = Quadrilateral((topLeft[1], topLeft[0]), (topRight[1], topRight[0]),
        (botLeft[1], botLeft[0]), (botRight[1], botRight[0]))
    topLeftAdd = uncropped.findFrac(uncropped.topLeft, uncropped.botLeft, 7/32)
    topRightAdd = uncropped.findFrac(uncropped.topRight, uncropped.botRight, 7/32)
    botLeftAdd = uncropped.findFrac(uncropped.botLeft, uncropped.topLeft, 7/32)
    botRightAdd = uncropped.findFrac(uncropped.botRight, uncropped.topRight, 7/32)

    #bilateral filter
    blur = cv2.bilateralFilter(image,9,75,75)
    #color balancing
    newBlur = simplest_cb(blur, 1)
    #convert to hsv
    img = np.array(cv2.cvtColor(newBlur, cv2.COLOR_BGR2HSV))
    #finds where the pattern starts
    topLeft1 = (topLeftAdd[0], topLeftAdd[1])
    topRight1 = (topRightAdd[0], topRightAdd[1])
    botLeft1 = (botLeftAdd[0], botLeftAdd[1])
    botRight1 = (botRightAdd[0], botRightAdd[1])
    print(topLeft1, topRight1, botLeft1, botRight1)

    #create quadrilateral
    #decode pattern
    fullPattern = Quadrilateral(topLeft1, topRight1, botLeft1, botRight1)
    colorRects = sixteenthArray(fullPattern)
    sorted = rearrange(colorRects)
    print(array_average_color(sorted, img))
    color_digits = colorsToNumbers(array_average_color(sorted, img))
    print(color_digits)
    color_digits_str = ""
    for num in color_digits:
        color_digits_str += str(num)
    print(color_digits_str)
    uin_str = code_to_uin(color_digits_str[::-1])
    if uin_str not in uin_array:
        uin_array.append(uin_str)
    return uin_str

img = cv2.imread('tester2.PNG')
#img = mpimg.imread('tester2.PNG')
#imgplot = plt.imshow(img)
#plt.show()
uin_str = master_runner(img, (514, 138), (36, 138), (40, 950), (504, 944))
print(uin_str)
print(uin_to_code("123456789"))
