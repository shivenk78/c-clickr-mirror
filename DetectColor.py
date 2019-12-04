from Quadrilateral import Quadrilateral

#takes a Quadrilateral and returns sixteen rectangles to find the average color of
def sixteenthArray(root):
    topRightQuarter = root.findQuarterQuad(1)
    topLeftQuarter = root.findQuarterQuad(2)
    botLeftQuarter = root.findQuarterQuad(3)
    botRightQuarter = root.findQuarterQuad(4)

    quarterArray = [topRightQuarter, topLeftQuarter, botLeftQuarter, botRightQuarter]
    colorRects = []
    for quarter in quarterArray:
        for i in range(1, 4):
            sixteenth = quarter.findQuarterQuad(i)
            print(str(sixteenth.topLeft) + " " + str(sixteenth.botRight) + "\n")
            colorRects.append(sixteenth.findRectFit())
    return colorRects

def array_average_color(root, image):
    color_array = []
    for rectangle in array:
        color_array.append(rectangle.getAverageColor(image))

topLeft = (0, 0)
topRight = (100, 0)
botLeft = (0, 100)
botRight = (100, 100)

fullPattern = Quadrilateral(topLeft, topRight, botLeft, botRight)

colorRects = sixteenthArray(fullPattern)
print(colorRects)
