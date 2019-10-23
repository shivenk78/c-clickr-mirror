from PIL import Image

colors = ["red", "green", "blue", "yellow"]
points = [[0, 75, 70, 175], [70, 75, 140, 175], [140, 75, 210, 175], [210, 75, 280, 175],
          [0, 175, 70, 275], [70, 175, 140, 275], [140, 175, 210, 275], [210, 175, 280, 275],
          [0, 275, 70, 375], [70, 275, 140, 375], [140, 275, 210, 375], [210, 275, 280, 375],
          [0, 375, 70, 475], [70, 375, 140, 475], [140, 375, 210, 475], [210, 375, 280, 475]]
codes = []
images = []
curCode = []

def toFour(code):
    codeFour = 0
    while (code != 0):
        codeFour *= 10
        codeFour += code % 4
        code = int(code / 4)
    code4Str = str(codeFour)
    for i in range(len(code4Str), 16):
        code4Str += "0"
    code4Str = code4Str[::-1]
    return code4Str

def toTen(a):
    a = a[::-1]
    uin = 0
    for i in range(16):
        dig = int(a[i])
        uin += dig * (4 ** i)
    print(uin)

def genImg(y):
    y = list(y)
    im = Image.new("RGB", (280, 550), "#FF05EE")
    codes.append(y.copy())
    for x in range(16):
        im.paste((colors[int(y[x])]), (points[x][0], points[x][1], points[x][2], points[x][3]))
    # black lines
    im.paste("black", (68, 75, 72, 475))
    im.paste("black", (138, 75, 142, 475))
    im.paste("black", (208, 75, 212, 475))
    im.paste("black", (0, 173, 280, 177))
    im.paste("black", (0, 273, 280, 277))
    im.paste("black", (0, 373, 280, 377))

    im.paste("turquoise", (0, 475, 280, 550))
    # im.show()
    images.append(im)
    return im

def show():
    print('Enter your UIN:')
    numImg = int(input())
    im = genImg(toFour((numImg)))
    im.show()

show()