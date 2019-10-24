import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Red color
    low_red = np.array([161, 50, 2])
    high_red = np.array([185, 255, 255])
    red_mask = cv2.inRange(hsv_frame, low_red, high_red)
    red = cv2.bitwise_and(frame, frame, mask=red_mask)
   

    # Green color
    low_green = np.array([25, 50, 0])
    high_green = np.array([102, 255, 255])
    green_mask = cv2.inRange(hsv_frame, low_green, high_green)
    green = cv2.bitwise_and(frame, frame, mask=green_mask)

    # Yellow color
    low_yellow = np.array([22,10,0])
    high_yellow= np.array([70,255,255])
    yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)
    yellow = cv2.bitwise_and(frame, frame, mask=yellow_mask)

     # Blue color
    low_blue = np.array([94, 80, 0])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv2.inRange(hsv_frame, low_blue, high_blue)
    red_blue_mask = cv2.bitwise_or(blue_mask, green_mask, red_mask, yellow_mask)
    blue = cv2.bitwise_and(frame, frame, mask=red_blue_mask)

    # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low, high)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow("Frame", frame)
    #cv2.imshow("Red", red)
    cv2.imshow("Blue", blue)
    #cv2.imshow("Green", green)
    #cv2.imshow("Result", result)

    key = cv2.waitKey(5)
    if key == 27:
        break
