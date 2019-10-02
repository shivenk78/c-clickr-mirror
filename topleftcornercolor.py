import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('test-image-v1.png', 0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

print(img[25, 25])
plt.show()
