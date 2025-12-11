from matplotlib import pyplot as plt
import numpy as np
import cv2
import plot_histogram
    
image = cv2.imread("parcel.jpeg")
cv2.imshow("Original", image)
plot_histogram.plot_histogram(image, "Histogram for Original Image")

mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Applying the Mask", masked)

plot_histogram.plot_histogram(image, "Histogram for Masked Image", mask = mask)
plt.show()
cv2.waitKey(0)
