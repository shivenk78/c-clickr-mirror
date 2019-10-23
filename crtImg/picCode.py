from PIL import Image

colors = ["red", "green", "blue", "yellow"]
points = [[0, 0, 70, 100], [70, 0, 140, 100], [140, 0, 210, 100], [210, 0, 280, 100],
          [0, 100, 70, 200], [70, 100, 140, 200], [140, 100, 210, 200], [210, 100, 280, 200],
          [0, 200, 70, 300], [70, 200, 140, 300], [140, 200, 210, 300], [210, 200, 280, 300],
          [0, 300, 70, 400], [70, 300, 140, 400], [140, 300, 210, 400], [210, 300, 280, 400]]
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
    im = Image.new("RGB", (280, 485), "#FF05EE")
    codes.append(y.copy())
    for x in range(16):
        im.paste((colors[int(y[x])]), (points[x][0], points[x][1], points[x][2], points[x][3]))
    # black lines
    im.paste("black", (68, 0, 72, 400))
    im.paste("black", (138, 0, 142, 400))
    im.paste("black", (208, 0, 212, 400))
    im.paste("black", (0, 98, 280, 102))
    im.paste("black", (0, 198, 280, 202))
    im.paste("black", (0, 298, 280, 302))
    # im.show()
    images.append(im)
    return im

def show():
    print('Enter your UIN:')
    numImg = int(input())
    im = genImg(toFour((numImg)))
    im.show()

show()