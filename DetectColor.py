import cv2

#Given the coordinates of the corners of the pattern
#Detects each of the colors in the pattern and where
#Colors stored in a list, snake style starting in upper left and ending in lower left

class Quadrilateral:
    def __init__(self, TL, TR, BL, BR):
        self.topLeft = TL
        self.topRight = TR
        self.botLeft = BL
        self.botRight = BR


    def findHalves(self, point1, point2):
        return (point1[0] + ((point2[0] - point1[0]) / 2), point1[1] + ((point2[1] - point1[1]) / 2))

    #num is 1-4 with 1 being top right and 4 being bottom right (like coord plane numbering)
    def findQuarterQuad(self, num):
        leftMiddle = self.findHalves(topLeft, botLeft)
        rightMiddle = self.findHalves(topRight, botRight)
        center = self.findHalves(leftMiddle, rightMiddle)
        if num == 1:
            return Quadrilateral(self.findHalves(self.topLeft, self.topRight), self.topRight, center, rightMiddle)
        elif num == 2:
            return Quadrilateral(self.topLeft, self.findHalves(self.topLeft, self.topRight), leftMiddle, center)
        elif num == 3:
            return Quadrilateral(leftMiddle, center, self.botLeft, self.findHalves(self.botLeft, self.botRight))
        elif num == 4:
            return Quadrilateral(center, rightMiddle, self.findHalves(self.botLeft, self.botRight), self.botRight)

    def findRectFit(self):
        if self.topLeft[0] > self.botLeft[0]:
            x1 = self.topLeft[0]
        else:
            x1 = self.botLeft[0]

        if self.topRight[0] > self.botRight[0]:
            x2 = self.botRight[0]
        else:
            x2 = self.topRight[0]

        if self.topLeft[1] > self.topRight[1]:
            y1 = self.topLeft[1]
        else:
            y1 = self.botLeft[1]

        if self.botLeft[1] > self.botRight[1]:
            y2 = self.botRight[1]
        else:
            y2 = self.botLeft[1]

        return ((x1, y1), (x2, y2))

    def sixteenthArray(self):
        topRightQuarter = self.findQuarterQuad(1)
        topLeftQuarter = self.findQuarterQuad(2)
        botLeftQuarter = self.findQuarterQuad(3)
        botRightQuarter = self.findQuarterQuad(4)

        quarterArray = [topRightQuarter, topLeftQuarter, botLeftQuarter, botRightQuarter]
        colorRects = []
        for quarter in quarterArray:
            for i in range(1, 4):
                sixteenth = quarter.findQuarterQuad(i)
                colorRects.append(sixteenth.findRectFit())

        return colorRects

topLeft = (0, 0)
topRight = (100, 0)
botLeft = (0, 100)
botRight = (100, 100)

fullPattern = Quadrilateral(topLeft, topRight, botLeft, botRight)
colorRects = fullPattern.sixteenthArray()
