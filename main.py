import cv2 
import numpy as np

img1 = cv2.imread("Images/test5.jpg")
img = cv2.resize(img1,(440,350))
kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,150,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Original image",img)
cv2.imshow("Gray image",imgGray)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialated Image",imgDialation)
cv2.imshow("Irotion Image",imgEroded)
cv2.waitKey(0)

