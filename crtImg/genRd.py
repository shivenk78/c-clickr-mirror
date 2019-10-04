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
    for z in codes:
        if z == cde:
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


for x in range(24):
    im = Image.new("RGB", (280, 500), "#FF05EE")
    while True:
        try:
            curCode = random.sample(range(0, 4), 4)
        except ValueError:
            print("Error with unique code generation")
        if checkCode(curCode):
            codes.append(curCode)
            break;
    for x in range(4):
        im.paste((colors[curCode[x]]), (points[x][0], points[x][1], points[x][2], points[x][3]))
    images.append(im)
for x in images:
    x.show()

# show that there are no duplicates
for x in codes:
    print(checkDupl(x))