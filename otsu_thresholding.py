import numpy as np
import cv2
import mahotas

image = cv2.imread("gulkok.jpg")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)
T = mahotas.thresholding.otsu(blurred)
print("Otsu’s threshold: {}".format(T))

thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_and(thresh, image)
cv2.imshow("Otsu", thresh)
T = mahotas.thresholding.rc(blurred)

c = cv2. 
print("Riddler-Calvard: {}".format(T))
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_or(thresh, T)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)

