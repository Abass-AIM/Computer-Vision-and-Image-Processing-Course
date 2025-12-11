import cv2

image = cv2.imread("parcel.jpeg")

blurred_1 = cv2.bilateralFilter(image, 5, 21, 21)
blurred_2 = cv2.bilateralFilter(image, 7, 31, 31)
blurred_3 = cv2.bilateralFilter(image, 9, 41, 41)

cv2.imshow("Bilateral Filter - d=5", blurred_1)
cv2.imshow("Bilateral Filter - d=7", blurred_2)
cv2.imshow("Bilateral Filter - d=9", blurred_3)

cv2.waitKey(0)


