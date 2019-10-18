from PIL import Image
import random

colors = ["red", "green", "blue", "yellow"]
points = [[0, 0, 140, 240], [140, 0, 280, 200], [0, 200, 140, 400], [140, 200, 280, 400]]
codes = []
images = []
curCode = []


# function redundant because using random.sample()
# but still wanted to implement because why not
def checkCode(cde):
    for z in cde:
        if z != 0 and z != 1 and z != 2 and z != 3:
            print('code must only have digits of 0-3')
            return False
    for z in cde:
        count = 0
        for y in cde:
            if y == z:
                count += 1
        if count > 1:
            print('code cannot have repeats of any of the digits')
            return False
    for z in codes:
        if z == cde:
            print('code should not have been entered before')
            return False
    return True


# test function to just make sure there are no duplicate images
def checkDupl(cde):
    count = 0
    for z in codes:
        if z == cde:
            count += 1
    if count > 1:
        return False
    return True


def printCodes():
    for x in codes:
        print(x)

def genImg(y):
    if checkCode(y):
        im = Image.new("RGB", (280, 500), "#FF05EE")
        codes.append(y.copy())
        for x in range(4):
            im.paste((colors[y[x]]), (points[x][0], points[x][1], points[x][2], points[x][3]))
        # im.show()
        images.append(im)

print('Enter the number of random images you want to generate up to 24:')
numImg = int(input())
print('Enter 0, 1, 2, and 3 in a random order:')
for i in range(numImg):
    for i in range(4):
        curCode.append(int(input("#: ")))
    print()
    genImg(curCode)
    curCode.clear()

# for x in range(24):
#     im = Image.new("RGB", (280, 500), "#FF05EE")
#     while True:
#         try:
#             curCode = random.sample(range(0, 4), 4)
#         except ValueError:
#             print("Error with unique code generation")
#         if checkCode(curCode):
#             codes.append(curCode)
#             break;
#     for x in range(4):
#         im.paste((colors[curCode[x]]), (points[x][0], points[x][1], points[x][2], points[x][3]))
#     images.append(im)
for x in images:
    x.show()

# show that there are no duplicates
# for x in codes:
#     print(checkDupl(x))

#print codes
printCodes()