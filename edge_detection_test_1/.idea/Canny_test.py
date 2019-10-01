import cv2
#
# from matplotlib import pyplot as plt

img = cv2.imread('test-image-v1.png', 0)

cv2.imshow('image', img)



# canny = cv2.Canny(img, 100, 200)
#
#
# titles = ['image']
# images = [img]
# for i in range(1):
#     plt.subplot(1, 1, i+1), plot,imshow(images[i], 'gray')
#     plt.xticks([]),plt.yticks([])
#
# plt.show()