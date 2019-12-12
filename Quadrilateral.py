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

    #same thing as findHalves but for other fractions
    def findFrac(self, point1, point2, fraction):
        return (point1[0] + ((point2[0] - point1[0]) * fraction), point1[1] + ((point2[1] - point1[1]) * fraction))

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
            x1 = self.topLeft[0] + ((self.topRight[0] - self.topLeft[0]) / 3)
        else:
            x1 = self.botLeft[0] + ((self.botRight[0] - self.botLeft[0]) / 3)

        if self.topRight[0] > self.botRight[0]:
            x2 = self.botRight[0] - ((self.botRight[0] - self.botLeft[0]) / 3)
        else:
            x2 = self.topRight[0] - ((self.topRight[0] - self.topLeft[0]) / 3)

        if self.topLeft[1] > self.topRight[1]:
            y1 = self.topLeft[1] + ((self.botLeft[1] - self.topLeft[1]) / 3)
        else:
            y1 = self.topRight[1] + ((self.botRight[1] - self.topRight[1]) / 3)

        if self.botLeft[1] > self.botRight[1]:
            y2 = self.botRight[1] - ((self.botRight[1] - self.topRight[1]) / 3)
        else:
            y2 = self.botLeft[1] - ((self.botLeft[1] - self.topLeft[1]) / 3)

        return Quadrilateral((x1,y1), (x2,y1), (x1,y2), (x2,y2))



    #finds the average color of a rectangle (will not work on other quadrilaterals)
    #image must be in hsv
    def getAverageColor(self, image):
        sum_hue = 0
        sum_sat = 0
        sum_val = 0
        count = 0
        if self.topLeft[0] < self.topRight[0]:
            first = self.topLeft[0]
            second = self.topRight[0]
        else:
            first = self.topRight[0]
            second = self.topLeft[0]

        if self.topLeft[1] < self.botLeft[1]:
            third = self.topLeft[1]
            fourth = self.botLeft[1]
        else:
            third = self.botLeft[1]
            fourth = self.topLeft[1]
        for x in range(int(first), int(second + 1)):
            for y in range(int(third), int(fourth + 1)):
                color = image[y,x]
                sum_hue += color[0]
                sum_sat += color[1]
                sum_val += color[2]
                count += 1
        return (int(sum_hue / count), int(sum_sat / count), int(sum_val / count))
