import numpy as np
import cv2
import imutils

image = cv2.imread("gandalf.png")

resized = imutils.resize(image, height = 50 , width = 100)
cv2.imshow("Resized via imutils Function", resized)
cv2.waitKey(0)
