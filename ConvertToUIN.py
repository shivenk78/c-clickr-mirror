#ConvertToUIN - given an array of HSV colors, convert to the student's UIN

# define color ranges
lower_blue = (241,50,50)
upper_blue = (300,255,255)

lower_red = (0,50,50)
upper_red = (60,255,255)

lower_green = (121,50,50)
upper_green = (180,255,255)

lower_yellow = (61,50,50)
upper_yellow = (120,255,255)

# assigns each color to digit in code
colorDict = {"red": 0, "green": 1, "blue": 2, "yellow": 3}

#converts array of colors to array of digits in code
#takes an array of tuples (3 elements)
def colorsToNumbers(array_of_colors):
    number_array = []
    for color in array_of_colors:
        if inRange(color, lower_red, upper_red):
            number_array.append(colorDict["red"])
        elif inRange(color, lower_green, upper_green):
            number_array.append(colorDict["green"])
        elif inRange(color, lower_blue, upper_blue):
            number_array.append(colorDict["blue"])
        elif inRange(color, lower_yellow, upper_yellow):
            number_array.append(colorDict["yellow"])

#finds if a color is in a certain color range
def inRange(color, lower, upper):
    for i in range(len(upper)):
        if !(lower[i]  <= color[i] <= upper[i]):
            return False
    return True
