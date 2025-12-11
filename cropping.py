import numpy as np
import cv2

image = cv2.imread("apple1.png")

cropped = image[30:120 , 240:335]
cv2.imshow("T-Rex Face", cropped)
cv2.waitKey(0)

