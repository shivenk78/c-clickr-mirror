import cv2

#Given the coordinates of the corners of the pattern
#Detects each of the colors in the pattern and where
#Colors stored in a list, snake style starting in upper left and ending in lower left

topLeft = (0, 0)
topRight = (100, 0)
botLeft = (0, 100)
botRight = (100, 100)

fullPattern = Quadrilateral(topLeft, topRight, botLeft, botRight)

topRightQuarter = fullPattern.findQuarterQuad(1)
topLeftQuarter = fullPattern.findQuarterQuad(2)
botLeftQuarter = fullPattern.findQuarterQuad(3)
botRightQuarter = fullPattern.findQuarterQuad(4)

pointsListX = []
pointsListY = []

for i in range (16):


class Quadrilateral:
    def __init__(TL, TR, BL, BR):
        topLeft = TL
        topRight = TR
        botLeft = BL
        botRight = BR


    def centroid(vertexes):
         _x_list = [vertex [0] for vertex in vertexes]
         _y_list = [vertex [1] for vertex in vertexes]
         _len = len(vertexes)
         _x = sum(_x_list) / _len
         _y = sum(_y_list) / _len
         return(_x, _y)

    def findHalves(point1, point2):
        return ((point2[0] - point1[0]) / 2, (point2[1] - point1[1]) / 2)

    #num is 1-4 with 1 being top right and 4 being bottom right (like coord plane numbering)
    def findQuarterQuad(num):
        leftMiddle = findHalves(topLeft, botLeft)
        rightMiddle = findHalves(topRight, botRight)
        center = findHalves(leftMiddle, rightMiddle)
        if num == 1:
            return Quadrilateral(findHalves(topLeft, topRight), topRight, center, rightMiddle)
        elif num == 2:
            return Quadrilateral(topLeft, findHalves(topLeft, topRight), leftMiddle, center)
        elif num == 3:
            return Quadrilateral(leftMiddle, center, botLeft, findHalves(botLeft, botRight))
        elif num == 4:
            return Quadrilateral(center, rightMiddle, findHalves(botLeft, botRight), botRight)
        else:
            return null
