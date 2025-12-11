import numpy as np
import cv2

image = cv2.imread("apple1.png")
w = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * w))
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

h = 50.0 / image.shape[0]
dim = (int(image.shape[1] * h), 50)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)
