import numpy as np

import cv2
# opening image 
img = cv2.imread("apple1.png")
cv2.imwrite("newimage.jpg",img)