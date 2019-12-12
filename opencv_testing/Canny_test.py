import cv2

import numpy as np

from matplotlib import pyplot as plt

# def nothing(x):
#
# img = np.zeros((300, 512, 3), np.uint8)
# cv2.namedWindow('adjust')
#
# cv2.createTrackbar('thresholdA', 'adjust', 0, 255, nothing)
#
#
#


# img = cv2.imread("/home/maxwelllwang/c-clickr/opencv_testing/test-image-v1.jpg", -1)
imgGs = cv2.imread("/home/maxwelllwang/c-clickr/opencv_testing/desk_test.jpg", 0)
img = cv2.imread("/home/maxwelllwang/c-clickr/opencv_testing/desk_test.jpg", -1)

sigmaString = input("input Sigma value")
sigma = float(sigmaString)
imgMedian = np.median(img)
lower = int(max(0, (1.0 - sigma) * imgMedian))
higher = int(max(255, (1.0 + sigma) * imgMedian))
print(higher)
print(lower)
cannyImg = cv2.Canny(img, lower, higher)
cannyImgGs = cv2.Canny(imgGs, lower, higher)

titles = ['image', 'imageGs', 'cannyImg']
images = [img, cannyImgGs, cannyImg]
for i in range(3):
    plt.subplot(1, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

while(1):
    cv2.imshow('adjust', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()

