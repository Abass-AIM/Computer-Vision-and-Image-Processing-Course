import numpy as np
import cv2

image = cv2.imread("parcel.jpeg")

# Apply different blur intensities
blur_3 = cv2.blur(image, (3, 3))
blur_5 = cv2.blur(image, (5, 5))
blur_7 = cv2.blur(image, (7, 7))

# Show separately
cv2.imshow("Blur (3x3)", blur_3)
cv2.imshow("Blur (5x5)", blur_5)
cv2.imshow("Blur (7x7)", blur_7)

cv2.waitKey(0)
