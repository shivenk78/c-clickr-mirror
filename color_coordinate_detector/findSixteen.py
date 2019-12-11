import cv2
import numpy as np
import math
import imutils
import time
import imgkit
from selenium import webdriver
from PIL import Image
import io
import numpy as np
from selenium.webdriver.firefox.options import Options

#
# browser = webdriver.Firefox()
# browser.get('http://10.192.81.85:8080/jsfs.html')
#
#
# print('1')
# data = browser.get_screenshot_as_png()
# while(1):
#     image = imgkit.from_url('http://10.192.81.85:8080/browserfs.htmlq', False)
#
#     data = Image.open(io.BytesIO(image))
#
#     img = np.asarray(data)
#
#
#     cv2.imshow('google', img)
#
#     if cv2.waitKey(10) & 0xFF == ord('q'):
#         # cap.release()
#         cv2.destroyAllWindows()
#         break
while (1):

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get("http://10.192.81.85:8080/browserfs.html")
    print("Headless Firefox Initialized")

    data = driver.get_screenshot_as_png()

    image = Image.open(io.BytesIO(data))



    img = np.array(image)
    red = img[:, :, 2].copy()
    blue = img[:, :, 0].copy()
    img[:, :, 0] = red
    img[:, :, 2] = blue

    cv2.imshow('google', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        # cap.release()
        cv2.destroyAllWindows()
        break

# while(1):
#     image = ImageGrab.grab()
#
#     # cv2.imshow("raw", image)
#     img = np.array(image)
#
#     # numpy be weird where blue and red are swapped
#     red = img[:, :, 2].copy()
#     blue = img[:, :, 0].copy()
#     img[:, :, 0] = red
#     img[:, :, 2] = blue
#
#     img = cv2.bilateralFilter(img, 9, 75, 75)
#
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#
#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#     thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
#
#     # find contours in the thresholded image and initialize the
#     # shape detector
#     cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
#                             cv2.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
#
#     squares = 0
#     for c in cnts:
#         peri = cv2.arcLength(c, True)
#         approx = cv2.approxPolyDP(c, 0.04 * peri, True)
#
#         if len(approx) == 4:
#             (x, y, w, h) = cv2.boundingRect(approx)
#             ar = w / float(h)
#
#             # a square will have an aspect ratio that is approximately
#             # equal to one, otherwise, the shape is a rectangle
#             if ar >= 0.95 and ar <= 1.05:
#                 squares = squares + 1
#     cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
#     cv2.imshow('ree', img)
#
#     print(squares)
