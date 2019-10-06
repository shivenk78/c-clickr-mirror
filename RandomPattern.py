import random
import time
from tkinter import *

master = Tk()

#set dimensions of canvas
canvas = Canvas(master, width=1000, height=1000)
canvas.pack()

#set dimensions of each quadrant
xDim = 100
yDim = xDim*2

#assign each digit in code to a color
colorDict = {0: "red", 1: "blue", 2: "yellow", 3: "green"}

def generatePattern() :
	canvas.delete("all")
	#generate 4-digit random code using all of 0,1,2,3
	code = [];
	while (len(code) < 4):
		i = random.randrange(0, 4)
		print(i)
		if not (i in code):
			code.append(i)
	print(code)
	
	#fill each quadrant with its respective color
	canvas.create_rectangle(0, 0, xDim, yDim, fill=colorDict[code[0]])
	canvas.create_rectangle(xDim, 0, xDim*2, yDim, fill=colorDict[code[1]])
	canvas.create_rectangle(0, yDim, xDim, yDim*2, fill=colorDict[code[2]])
	canvas.create_rectangle(xDim, yDim, xDim*2, yDim*2, fill=colorDict[code[3]])
	canvas.create_rectangle(0, yDim*2, xDim*2, yDim*2+yDim*(1/4), fill="purple")

	master.update()
	master.after(500, generatePattern)	

master.after(0, generatePattern)
mainloop()