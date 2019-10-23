import random
import time
import tkinter as tk

master = tk.Tk()

#sets dimensions of canvas
canvas = tk.Canvas(master, width=1000, height=1000)
canvas.pack()

#sets dimensions of each quadrant
xDim = 150
yDim = xDim*2

#assigns each digit in code to a color 
colorDict = {0: "red", 1: "blue", 2: "yellow", 3: "green"}

#generates pattern with a given code
def generatePattern(newCodeStr) :
	print(newCodeStr)
	canvas.delete("all")

	code = [int(newCodeStr[0]),int(newCodeStr[1]),int(newCodeStr[2]),int(newCodeStr[3])]

	#fills each quadrant with its respective color
	canvas.create_rectangle(0, 0, xDim, yDim, fill=colorDict[code[0]])
	canvas.create_rectangle(xDim, 0, xDim*2, yDim, fill=colorDict[code[1]])
	canvas.create_rectangle(0, yDim, xDim, yDim*2, fill=colorDict[code[2]])
	canvas.create_rectangle(xDim, yDim, xDim*2, yDim*2, fill=colorDict[code[3]])
	canvas.create_rectangle(0, yDim*2, xDim*2, yDim*2+yDim*(1/4), fill="purple")

	#sets title of window as 4-digit code
	master.title(newCodeStr)
	master.update()

#generates pattern based on user input
def generateInputPattern() :
    inputStr = input("Enter a 4-digit code XXXX using [0,1,2,3]: ")

    generatePattern(inputStr)

#generates random pattern
def generateRandomPattern() :
	codeStr = ""
	while (len(codeStr) < 4):
		codeStr += str(random.randrange(0, 4))

	generatePattern(codeStr)

#generates random patterns in fixed time intervals
def generateContinuousRandomPattern() :
	generateRandomPattern()
	timeDiff = 500
	master.after(timeDiff, generateContinuousRandomPattern)  

mode = input("Select mode: input (i), random (r), continuous random (c): ")
chooseMode = {
        "i": generateInputPattern,
        "r": generateRandomPattern,
        "c": generateContinuousRandomPattern
}
try:
        func = chooseMode.get(mode)
        func()
except:
        print("Invalid mode")

tk.mainloop()
