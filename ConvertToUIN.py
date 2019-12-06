#ConvertToUIN - given an array of HSV colors, convert to the student's UIN

# define color ranges
lower_yellow = (25,50,50)
upper_yellow = (50,255,255)

lower_red = (0,50,50)
upper_red = (24,255,255)

lower_red_2 = (150,50,50)
upper_red_2 = (179,255,255)

lower_green = (51,50,50)
upper_green = (80,255,255)

lower_blue = (81,50,50)
upper_blue = (149,255,255)

# assigns each color to digit in code
colorDict = {"red": 0, "green": 1, "blue": 2, "yellow": 3}

#converts array of colors to array of digits in code
#takes an array of tuples (3 elements)
def colorsToNumbers(array_of_colors):
    number_array = []
    for color in array_of_colors:
        if inRange(color, lower_red, upper_red) or inRange(color, lower_red_2, upper_red_2):
            number_array.append(colorDict["red"])
        elif inRange(color, lower_green, upper_green):
            number_array.append(colorDict["green"])
        elif inRange(color, lower_blue, upper_blue):
            number_array.append(colorDict["blue"])
        elif inRange(color, lower_yellow, upper_yellow):
            number_array.append(colorDict["yellow"])
    return number_array

# converts base 4 code to base 10 UIN
def code_to_uin(new_code_str):
    uin_str = str(int(new_code_str, 4))
    while len(uin_str) < 9:
        uin_str = "0" + uin_str

    return uin_str

#finds if a color is in a certain color range
def inRange(color, lower, upper):
    for i in range(len(color)):
        if lower[i] > color[i] or color[i] > upper[i]:
            return False
    return True
