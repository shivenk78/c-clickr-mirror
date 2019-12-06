#Quadrialteral Class - stores the corners (x, y) of a quadrilateral
#                    - methods to split the quadrialteral into equal portions (grid)

import cv2
from imutils.video import VideoStream

class Quadrilateral:
    #initializes variables
    def __init__(self, TL, TR, BL, BR):
        self.topLeft = TL
        self.topRight = TR
        self.botLeft = BL
        self.botRight = BR

    #finds the halfway point of a line drawn between two points
    def findHalves(self, point1, point2):
        return (point1[0] + ((point2[0] - point1[0]) / 2), point1[1] + ((point2[1] - point1[1]) / 2))

    #returns a quarter of the quadrilateral, coordinate plane style (return first quadrant etc.)
    #num is 1-4 with 1 being top right and 4 being bottom right (like coord plane numbering)
    def findQuarterQuad(self, num):
        leftMiddle = self.findHalves(self.topLeft, self.botLeft)
        rightMiddle = self.findHalves(self.topRight, self.botRight)
        center = self.findHalves(leftMiddle, rightMiddle)
        if num == 2:
            return Quadrilateral(self.findHalves(self.topLeft, self.topRight), self.topRight, center, rightMiddle)
        elif num == 1:
            return Quadrilateral(self.topLeft, self.findHalves(self.topLeft, self.topRight), leftMiddle, center)
        elif num == 3:
            return Quadrilateral(leftMiddle, center, self.botLeft, self.findHalves(self.botLeft, self.botRight))
        elif num == 4:
            return Quadrilateral(center, rightMiddle, self.findHalves(self.botLeft, self.botRight), self.botRight)

    #returns a rectange completely within the bounds of the quadrilateral
    #rectangle is NOT maximized, just want the area towards the center of the quadrilateral
    def findRectFit(self):
        if self.topLeft[0] > self.botLeft[0]:
            x1 = self.topLeft[0] + ((self.topRight[0] - self.topLeft[0]) / 4)
        else:
            x1 = self.botLeft[0] + ((self.botRight[0] - self.botLeft[0]) / 4)

        if self.topRight[0] > self.botRight[0]:
            x2 = self.botRight[0] - ((self.botRight[0] - self.botLeft[0]) / 4)
        else:
            x2 = self.topRight[0] - ((self.topRight[0] - self.topLeft[0]) / 4)

        if self.topLeft[1] > self.topRight[1]:
            y1 = self.topLeft[1] + ((self.botLeft[1] - self.topLeft[1]) / 4)
        else:
            y1 = self.topRight[1] + ((self.botRight[1] - self.topRight[1]) / 4)

        if self.botLeft[1] > self.botRight[1]:
            y2 = self.botRight[1] - ((self.botRight[1] - self.topRight[1]) / 4)
        else:
            y2 = self.botLeft[1] - ((self.botLeft[1] - self.topLeft[1]) / 4)

        return ((x1, y1), (x2, y2))

    #finds the average color of a rectangle (will not work on other quadrilaterals)
    #image must be in hsv
    def getAverageColor(self, image):
        sum_hue = 0
        sum_sat = 0
        sum_val = 0
        count = 0
        for x in range(topLeft[0], topRight[0] + 1):
            for y in range(topLeft[1], botLeft[1] + 1):
                color = int(image[x,y])
                sum_hue += color[0]
                sum_sat += color[1]
                sum_val += color[2]
                count += 1
        return int(sum_hue / count, sum_sat / count, sum_val / count)
