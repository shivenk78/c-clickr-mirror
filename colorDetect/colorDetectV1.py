import cv2 
import numpy as np  
  
cap = cv2.VideoCapture(0)  
  
while(1):        
    # Captures the live stream frame-by-frame 
    _, frame = cap.read()  
    # Converts images from BGR to HSV 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_pink = np.array([130,50,70])
    upper_pink = np.array([150,255,255])

    lower_blue = np.array([100,50,50])
    upper_blue = np.array([125,255,255])

    lower_red = np.array([160,50,50])
    upper_red = np.array([190,255,255])

    lower_green = np.array([70,50,50])
    upper_green = np.array([100,255,255])

    lower_yellow = np.array([70,50,50])
    upper_yellow = np.array([100,255,255])

    # Define color range
    pink_mask = cv2.inRange(hsv, lower_pink, upper_pink) 
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    super_mask = cv2.bitwise_or(pink_mask, blue_mask)
    super_mask = cv2.bitwise_or(super_mask, red_mask)
    super_mask = cv2.bitwise_or(super_mask, green_mask)
    
    # Color Masking
    res = cv2.bitwise_and(frame,frame, mask= super_mask) 
    cv2.imshow('frame',frame) 
    cv2.imshow('mask',super_mask) 
    cv2.imshow('res',res) 
    
    # Shows the 3 different camera views in separate windows
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break
  
# Destroys all of the HighGUI windows, then releases the frame
cv2.destroyAllWindows() 
cap.release() 