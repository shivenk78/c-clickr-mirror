import cv2

tstImg = cv2.imread("/home/maxwelllwang/c-clickr/opencv_testing/camShiftTest.jpg")

print(tstImg)

cv2.imshow('pic', tstImg)
cv2.waitKey()
cv2.destroyAllWindows()
