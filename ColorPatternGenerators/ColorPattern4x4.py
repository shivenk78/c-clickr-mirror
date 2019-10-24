# NOTE: code = 16-digit base 4 number ; uin = 9-digit base 10 number

import random
import tkinter as tk

master = tk.Tk()

# sets dimensions of canvas
canvas = tk.Canvas(master, width=1000, height=1000)
canvas.pack()

# sets dimensions of each quadrant
xDim = 100
yDim = int(xDim * 1.5)
xTotal = xDim * 4
yTotal = yDim * 4
yStart = yDim / 2

# assigns each digit in code to a color
colorDict = {0: "red", 1: "green", 2: "blue", 3: "yellow"}


# generates pattern with a given code
def generate_pattern(new_code_str):
    to_string = "Code: %s, UIN: %s" % (new_code_str, code_to_uin(new_code_str))

    canvas.delete("all")

    # converts code string to list
    code = []
    for i in range(len(new_code_str)):
        code.append(int(new_code_str[i]))

    # fills each quadrant with its respective color
    count = 0
    for j in range(0, yTotal, yDim):
        for i in range(0, xTotal, xDim):
            canvas.create_rectangle(i, yStart + j, i + xDim, yStart + j + yDim, fill=colorDict[code[count]])
            count = count + 1
    canvas.create_rectangle(0, 0, xTotal, yStart, fill="magenta")
    canvas.create_rectangle(0, yStart + yTotal, xTotal, yTotal + yDim, fill="cyan")

    # displays 16-digit code and 9-digit UIN in title
    print(to_string)
    master.title(to_string)
    master.update()


# generates pattern based on user input code
def generate_code_input_pattern():
    code_input_str = input("Enter a 16-digit code XXXXXXXXXXXXXXXX using [0-3]: ")
    print(code_input_str)

    generate_pattern(str(code_input_str))


# generates pattern based on user input UIN
def generate_uin_input_pattern():
    uin_input_str = input("Enter a 9-digit UIN XXXXXXXXXX using [0-9]: ")

    generate_pattern(uin_to_code(str(uin_input_str)))


# generates random pattern
def generate_random_pattern():
    code_str = ""
    while len(code_str) < 16:
        code_str += str(random.randrange(0, 4))

    generate_pattern(code_str)


# generates random patterns in fixed time intervals
def generate_continuous_random_pattern():
    time_diff = 500

    generate_random_pattern()
    master.after(time_diff, generate_continuous_random_pattern)


# converts base 4 code to base 10 UIN
def code_to_uin(new_code_str):
    uin_str = str(int(new_code_str, 4))
    while len(uin_str) < 9:
        uin_str = "0" + uin_str

    return uin_str


# converts base 10 UIN to base 4 code
def uin_to_code(new_uin_str):
    code = 0
    uin = int(new_uin_str)
    multiplier = 1

    while uin != 0:
        code += (uin % 4) * multiplier
        uin = int(uin / 4)
        multiplier *= 10

    code_str = str(code)
    while len(code_str) < 16:
        code_str = "0" + code_str

    return code_str


mode = input("Select mode: input code (ic), input UIN (iu), random (r), continuous random (cr): ")
choose_mode = {
    "ic": generate_code_input_pattern,
    "iu": generate_uin_input_pattern,
    "r": generate_random_pattern,
    "cr": generate_continuous_random_pattern
}


try:
    func = choose_mode.get(mode)
    func()
except:
    print("Error")

tk.mainloop()
