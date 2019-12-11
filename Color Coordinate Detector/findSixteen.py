import cv2
import numpy as np
import pyscreenshot as ImageGrab
import math
import time
import imutils


while(1):
    image = ImageGrab.grab();
    img = np.array(image)
    orig = img.copy()

    # numpy be weird where blue and red are swapped
    red = img[:, :, 2].copy()
    blue = img[:, :, 0].copy()
    img[:, :, 0] = red
    img[:, :, 2] = blue

    img = cv2.bilateralFilter(img, 9, 75, 75)


