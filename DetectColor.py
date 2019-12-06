#DetectColor - used to divide a Quadrilateral into sixteenths and find the average color
#            - (turning given Quadrilateral into array of colors)

from Quadrilateral import Quadrilateral
from ConvertToUIN import *
import numpy as np
import cv2

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

def master_runner(image):
    blur = cv2.bilateralFilter(image,9,75,75)
    img = np.array(cv2.cvtColor(blur, cv2.COLOR_BGR2HSV))
    topLeft = (0, 0)
    topRight = (len(img), 0)
    botLeft = (0, len(img[0]))
    botRight = (len(img), len(img[0]))

    fullPattern = Quadrilateral(topLeft, topRight, botLeft, botRight)
    colorRects = sixteenthArray(fullPattern)
    sorted = rearrange(colorRects)
    print(array_average_color(sorted, img))
    color_digits = colorsToNumbers(array_average_color(sorted, img))
    print(color_digits)
    color_digits_str = ""
    for num in color_digits:
        color_digits_str += str(num)
    print(color_digits_str)
    return code_to_uin(color_digits_str)

img = cv2.imread('test_image.png')
print(master_runner(img))
