

import cv2

image=cv2.imread("apple1.png")

(b, g, r) = image[0, 0]

image[0, 0] = (0, 0, 255)
image[1, 0] = (0, 0, 255)
image[2, 0] = (0, 0, 255)
image[0, 1] = (0, 0, 255)
image[0, 2] = (0, 0, 255)

image[1, 2] = (0, 0, 255)
image[2, 1] = (0, 0, 255)
image[2, 2] = (0, 0, 255)

(b, g, r) = image[0, 0]

cv2.imshow("Image", image)
cv2.waitKey(0)