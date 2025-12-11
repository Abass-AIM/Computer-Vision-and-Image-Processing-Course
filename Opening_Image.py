import numpy as np

import cv2
# opening image 
img = cv2.imread("apple1.png")
#Saving new image
cv2.imwrite("new_apple.jpg",img)