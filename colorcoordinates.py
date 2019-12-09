''' 
- Currently gives all distances where the magenta and cyan are at a large enough area so it should not track background noise
- Will give ALL distances between including distances between the magenta and cyan of two completely different patters. 
- for some reason I refer to magenta as red and cyan as blue for most of this code
- VSCode shows cv2 underlined in red but it works so...
'''
#importing modules

import cv2
import numpy as np
import math
import imutils

#create class to store pattern objects
class pattern:
        def __init__(self, id,  magenta, cyan, distance):
                self.id = id
                self.top = magenta
                self.bottom = cyan
                self.distance = distance
class coordinates:
        def __init__(self, x, y):
                self.x = x
                self.y = y
def rotatePoint(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy
#capturing video through webcam
cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
cap.set(cv2.CAP_PROP_AUTO_WB, 0)

#list of distances found
patternList = []

#can give each distance a unique id???
idCount = 0

while(1):
        _, img = cap.read()

        img = cv2.bilateralFilter(img, 11, 75, 75)

        #list is cleared for each run through
        patternList = []
            
        #converting frame(img i.e BGR) to HSV (hue-saturation-value)
        hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        #find center of image
        (h, w) = img.shape[:2]
        centerImage = (w // 2, h // 2)

        #definig the range of magenta color
        red_lower=np.array([147,115,150],np.uint8)
        red_upper=np.array([150,255,255],np.uint8)

        #defining the Range of cyan color
        blue_lower=np.array([87,115,150],np.uint8)
        blue_upper=np.array([93,255,255],np.uint8)

        #finding the range of magenta,cyan and other colors in the image
        red=cv2.inRange(hsv, red_lower, red_upper)
        blue=cv2.inRange(hsv, blue_lower, blue_upper)

        
        #Morphological transformation, Dilation
        kernal = np.ones((5 ,5), "uint8")

        red=cv2.dilate(red, kernal)
        res=cv2.bitwise_and(img, img, mask = red)

        blue=cv2.dilate(blue,kernal)
        res1=cv2.bitwise_and(img, img, mask = blue)

        # variables to store the coordinates
        redX = 0
        redY = 0
        blueX = 0
        blueY = 0

        #Tracking the Red Color
        (contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
                redArea = cv2.contourArea(contour)
                if(redArea>400):
                        x,y,w,h = cv2.boundingRect(contour)

                        #draws rectangle and label
                        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                        cv2.putText(img,"top color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))

                        #finds centroid and draws it
                        M = cv2.moments(contour)
                        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                        cv2.putText(img,"("+str(center[0])+","+str(center[1])+")", (center[0]+10,center[1]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(0, 0, 255),1)
                        redX = center[0]
                        redY = center[1]
                        cv2.circle(img, center, 2, (0, 0, 0))

                        #for each Red contour, loop through blue and compare distance (tested other methods and this works best)
                        (contoursBlue,hierarchyBlue)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                        for pic, contour in enumerate(contoursBlue):
                                blueArea = cv2.contourArea(contour)
                                if(abs(blueArea) > 400):
                                        x,y,w,h = cv2.boundingRect(contour)     
                                        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                                        cv2.putText(img,"bottom color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
                                        M = cv2.moments(contour)
                                        centerBlue = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                                        cv2.putText(img,"("+str(center[0])+","+str(center[1])+")", (center[0]+10,center[1]+15), cv2.FONT_HERSHEY_SIMPLEX, 0.4,(255, 0, 0),1)
                                        blueX = centerBlue[0]
                                        blueY = centerBlue[1]
                                        cv2.circle(img, centerBlue, 2, (0, 0, 0))
                                        
                                        # if either coordinate is (0,0) that means it is not found and should not be appended to the list
                                        if not(redX == 0 and redY == 0) and not(blueX == 0 and blueY == 0):
                                                distance = math.sqrt( ((redX-blueX)**2)+((redX-blueX)**2) )

                                                #create object and append to the list
                                                #first create two coordinate objects and then add that to the pattern object
                                                magenta = coordinates(redX, redY)
                                                cyan = coordinates(blueX, blueY)
                                                p1 = pattern(idCount, magenta, cyan, distance)
                                                patternList.append(p1)
                                                idCount = idCount + 1
        #show each distance calculated
        crop_img = img
        for thing in patternList:
                #cv2.line(img, (thing.top.x, thing.top.y), (thing.bottom.x, thing.bottom.y), (0,0,0), 5)
                print("(" + str(thing.top.x) + "," + str(thing.top.y) + ")\t" + "(" + str(thing.bottom.x) + "," + str(thing.bottom.y) + ")\t" + "Distance:" + str(thing.distance))
                # #find angle
                # print abs(thing.bottom.y - thing.top.y)
                # print abs(thing.bottom.x - thing.top.x)
                colorAngleRad = math.atan2((thing.bottom.y - thing.top.y), (thing.bottom.x - thing.top.x))
                colorAngle = math.degrees(colorAngleRad)
                
                print "Radian" + str(colorAngleRad)
                print "degrees" + str(int(colorAngle))

                #rotate cropped image
                if colorAngle != 0:
                        rot_img = imutils.rotate(img, int(colorAngle))
                (rotx, roty) = rotatePoint(centerImage, (thing.top.x, thing.top.y), colorAngleRad)
                (rotx1, roty1) = rotatePoint(centerImage, (thing.bottom.x, thing.bottom.y), colorAngleRad)
                cv2.circle(rot_img, (int(rotx), int(roty)), 7, (0, 255, 0), 4)
                cv2.circle(rot_img, (int(rotx1), int(roty1)), 7, (255, 255, 255), 4)
                cv2.imshow("Rotated" ,rot_img)       
                #check for 0 division
                #does not rotate if cyan is lower than magenta
                # if (thing.bottom.x > thing.bottom.y):
                #         colorAngleRad = math.atan((thing.bottom.y - thing.top.y) / (thing.bottom.x - thing.top.x))
                #         colorAngle = math.degrees(colorAngleRad)
                #         print colorAngle
                #         print int(colorAngle)
                #         #rotate cropped image
                #         if colorAngle != 0:
                #                 for angle in xrange(0, 360, int(colorAngle + 360)):
                #                         # rotate the image and display it
                #                         crop_img = imutils.rotate(img, angle=int(colorAngle + 360))

                #                         #set new pixel coordinates!!!
                #                         #thing.bottom.x = imutils.rotate()
                #                 (rotx, roty) = rotatePoint(centerImage, (thing.top.x, thing.top.y), colorAngleRad + 2*math.pi)
                #                 #(thing.bottom.x, thing.bottom.y) = rotatePoint((thing.bottom.x, thing.bottom.y), colorAngleRad + 2*math.pi, center)

                #                 # thing.top.y = int(thing.top.y)
                #                 # thing.bottom.y = int(thing.bottom.y)
                #                 # thing.top.x = int(thing.top.x)
                #                 # thing.bottom.x = int(thing.bottom.x)
                #                 # cv2.circle(crop_img, (int(rotx), int(roty)), 7, (255, 0, 0))
                #                 # cv2.circle(crop_img, (int(thing.top.x), int (thing.top.y)), 5, (0, 255, 0))
                #                 # cv2.circle(img, (int(thing.top.x), int (thing.top.y)), 3, (0, 0, 0))

                #                 cv2.imshow("Rotated" ,crop_img)
                # if thing.top.x < thing.bottom.x:
                #         dist = int((thing.bottom.x - thing.top.x) / (5 / 2))
                #         crop_img = crop_img[abs(thing.top.y - dist) :thing.top.y + dist, thing.top.x :thing.bottom.x]
                # else:
                #         dist = int((thing.top.x - thing.bottom.x) / (5 / 2))
                #         crop_img = crop_img[abs(thing.top.y - dist) :thing.top.y + dist, thing.bottom.x :thing.top.x]

                # gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
                # #cv2.imshow("gray", gray)

                # blur = cv2.GaussianBlur(gray, (5,5), 0)
                # #cv2.imshow("blur", blur)

                # thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
                # #cv2.RETR_TREE
                # (contours, ok1) = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                # #(contoursExternal, ok1) = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # c = 0
                # for i in contours:
                #         area = cv2.contourArea(i)
                #         if area > 1000/2:
                #                 cv2.drawContours(crop_img, contours, c, (0, 255, 0), 3)
                #                 #cv2.drawContours(crop_img, contoursExternal, c, (0, 0, 255), 3)
                #         c+=1
                
                #cv2.imshow("cropped", crop_img)

                # cv2.imshow("cropped", thresh)
                # print("(" + str(thing.top.x) + "," + str(thing.top.y) + ")\t" + "(" + str(thing.bottom.x) + "," + str(thing.bottom.y) + ")\t" + "Distance:" + str(thing.distance))

        #cv2.imshow("Redcolour",red)
        cv2.imshow("Color Tracking",img)
        #img = cv2.flip(img,1)
        #cv2.imshow("red",res)
        if cv2.waitKey(10) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break