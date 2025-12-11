import cv2

image = cv2.imread("parcel.jpeg")

blurred_3 = cv2.medianBlur(image, 3)
blurred_5 = cv2.medianBlur(image, 5)
blurred_7 = cv2.medianBlur(image, 7)

cv2.imshow("Median Blur - k=3", blurred_3)
cv2.imshow("Median Blur - k=5", blurred_5)
cv2.imshow("Median Blur - k=7", blurred_7)

cv2.waitKey(0)

