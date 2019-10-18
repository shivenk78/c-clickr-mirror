import random
import time
import tkinter as tk

master = tk.Tk()

#sets dimensions of canvas
canvas = tk.Canvas(master, width=1000, height=1000)
canvas.pack()

#sets dimensions of each quadrant
xDim = 100
yDim = xDim*2

#assigns each digit in code to a color 
colorDict = {0: "red", 1: "blue", 2: "yellow", 3: "green"}

#generates pattern with a given code
def generatePattern(newCode) :
	canvas.delete("all")

	#fills each quadrant with its respective color
	canvas.create_rectangle(0, 0, xDim, yDim, fill=colorDict[newCode[0]])
	canvas.create_rectangle(xDim, 0, xDim*2, yDim, fill=colorDict[newCode[1]])
	canvas.create_rectangle(0, yDim, xDim, yDim*2, fill=colorDict[newCode[2]])
	canvas.create_rectangle(xDim, yDim, xDim*2, yDim*2, fill=colorDict[newCode[3]])
	canvas.create_rectangle(0, yDim*2, xDim*2, yDim*2+yDim*(1/4), fill="purple")

	#sets title of window as 4-digit code
	newStr = ""
	for i in newCode:
		newStr += str(i)
	master.title(newStr)

	master.update()

#generates pattern based on user input
def generateInputPattern() :
        inputStr = input("Enter a 4-digit code XXXX using [0,1,2,3]: ")
        inputCode = [int(inputStr[0]),int(inputStr[1]),int(inputStr[2]),int(inputStr[3])]
        print(inputCode)
        
        generatePattern(inputCode)

#generates random pattern
def generateRandomPattern() :
	#generate 4-digit random code using all of 0,1,2,3
	code = [];
	while (len(code) < 4):
		code.append(random.randrange(0, 4))
	print(code)

	generatePattern(code)

#generates random patterns in fixed time intervals
def generateContinuousRandomPattern() :
	generateRandomPattern()
	timeDiff = 500
	master.after(timeDiff, generateContinuousRandomPattern)  

mode = input("Select mode: input (I), random (R), continuous random (CR): ")
chooseMode = {
        "I": generateInputPattern,
        "R": generateRandomPattern,
        "CR": generateContinuousRandomPattern
}
try:
        func = chooseMode.get(mode)
        func()
except:
        print("Invalid mode")

tk.mainloop()
