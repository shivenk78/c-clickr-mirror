import cv2

#Given the coordinates of the corners of the pattern
#Detects each of the colors in the pattern and where
#Colors stored in a list, snake style starting in upper left and ending in lower left

topLeft = (0, 0)
topRight = (100, 0)
botLeft = (0, 100)
botRight = (100, 100)

incrementLeftEdge = (botLeft - topLeft) / 4
incrementRightEdge = (botRight - topRight) / 4
incrementTopEdge = (topRight - topLeft) / 4
incrementBotEdge = (botRight - botLeft) / 4
