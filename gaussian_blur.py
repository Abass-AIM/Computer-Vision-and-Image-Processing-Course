

import cv2

image = cv2.imread("parcel.jpeg")

blurred_3 = cv2.GaussianBlur(image, (3, 3), 0)
blurred_5 = cv2.GaussianBlur(image, (5, 5), 0)
blurred_7 = cv2.GaussianBlur(image, (7, 7), 0)

cv2.imshow("Gaussian Blur - 3x3", blurred_3)
cv2.imshow("Gaussian Blur - 5x5", blurred_5)
cv2.imshow("Gaussian Blur - 7x7", blurred_7)

cv2.waitKey(0)
cv2.destroyAllWindows()
