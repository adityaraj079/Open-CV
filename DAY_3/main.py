import cv2 
import numpy as np

img1 = cv2.imread("Images/test2.jpg")


width,height = 250,350
pts1 = np.float32([[161,677],[749,653],[121,1037],[737,1049]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img1,matrix,(width,height))

img = cv2.resize(img1,(440,350))
cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)
