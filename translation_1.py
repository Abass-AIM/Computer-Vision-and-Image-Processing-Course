import numpy as np
import cv2
import imutils

image = cv2.imread("gandalf.png")
cv2.imshow("original", image)

shifted = imutils.translate(image, 5, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
