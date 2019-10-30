#importing modules

import cv2
import numpy as np
import math

#capturing video through webcam
cap=cv2.VideoCapture(0)


while(1):
	_, img = cap.read()
	    
	#converting frame(img i.e BGR) to HSV (hue-saturation-value)

	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	#definig the range of red color
	red_lower=np.array([136,87,111],np.uint8)
	red_upper=np.array([180,255,255],np.uint8)

	#defining the Range of Blue color
	blue_lower=np.array([99,115,150],np.uint8)
	blue_upper=np.array([120,255,255],np.uint8)

	'''
	#defining the Range of yellow color
	yellow_lower=np.array([22,60,200],np.uint8)
	yellow_upper=np.array([60,255,255],np.uint8)
	'''

	#finding the range of magenta,cyan and other colors in the image
	red=cv2.inRange(hsv, red_lower, red_upper)
	blue=cv2.inRange(hsv, blue_lower, blue_upper)
	#yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
	
	#Morphological transformation, Dilation
	kernal = np.ones((5 ,5), "uint8")

	red=cv2.dilate(red, kernal)
	res=cv2.bitwise_and(img, img, mask = red)

	blue=cv2.dilate(blue,kernal)
	res1=cv2.bitwise_and(img, img, mask = blue)

	'''
	yellow=cv2.dilate(yellow,kernal)
	res2=cv2.bitwise_and(img, img, mask = yellow)
        '''
	redX = 0;
	redY = 0;
	#Tracking the Red Color
	(contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			
			x,y,w,h = cv2.boundingRect(contour)
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"top color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
			M = cv2.moments(contour)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			cv2.putText(img,"("+str(center[0])+","+str(center[1])+")", (center[0]+10,center[1]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 255),1)
			redX = center[0];
			redY = center[1];
	blueX = 0;
	blueY = 0;
        #Tracking the blue Color
	(contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			x,y,w,h = cv2.boundingRect(contour)	
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			cv2.putText(img,"bottom color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
			M = cv2.moments(contour)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			cv2.putText(img,"("+str(center[0])+","+str(center[1])+")", (center[0]+10,center[1]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(255, 0, 0),1)
			blueX = center[0];
			blueY = center[1];
	distance = math.sqrt( ((redX-blueX)**2)+((redX-blueX)**2) )
	print("(" + str(redX) + "," + str(redY) + ")\t" + "(" + str(blueX) + "," + str(blueY) + ")\t" + "Distance:" + str(distance))
	'''
	#Tracking the yellow Color
	(contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			x,y,w,h = cv2.boundingRect(contour)	
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
			cv2.putText(img,"yellow  color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0))

        '''  
    	#cv2.imshow("Redcolour",red)
	cv2.imshow("Color Tracking",img)
	img = cv2.flip(img,1)
    	#cv2.imshow("red",res)
	if cv2.waitKey(10) & 0xFF == ord('q'):
    		cap.release()
    		cv2.destroyAllWindows()
    		break
