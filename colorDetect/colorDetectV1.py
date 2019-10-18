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
  
    # Define color range
    mask = cv2.inRange(hsv, lower_pink, upper_pink) 
    
    # Color Masking
    res = cv2.bitwise_and(frame,frame, mask= mask) 
    cv2.imshow('frame',frame) 
    cv2.imshow('mask',mask) 
    cv2.imshow('res',res) 
    
    # Shows the 3 different camera views in separate windows
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break
  
# Destroys all of the HighGUI windows. 
cv2.destroyAllWindows() 
  
# release the captured frame 
cap.release() 