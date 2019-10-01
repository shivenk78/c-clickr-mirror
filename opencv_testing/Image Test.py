import cv2

tstImg = cv2.imread("/home/maxwelllwang/c-clickr/opencv_testing/test-image-v1.jpg", 0)

print(tstImg)

cv2.imshow('pic', tstImg)
cv2.waitKey(6000)
cv2.destroyAllWindows()
