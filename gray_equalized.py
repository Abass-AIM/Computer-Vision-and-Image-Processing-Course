import numpy as np
import cv2
from matplotlib import pyplot as plt

# Read image and convert to grayscale
image = cv2.imread("parcel.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
eq = cv2.equalizeHist(gray)

# Compute histograms
hist_original = cv2.calcHist([gray], [0], None, [256], [0, 256])
hist_equalized = cv2.calcHist([eq], [0], None, [256], [0, 256])

# Plot images and histograms
plt.figure(figsize=(12,6))

# Original image and histogram
plt.subplot(2,2,1)
plt.imshow(gray, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2,2,2)
plt.plot(hist_original, color='black')
plt.title('Original Histogram')
plt.xlim([0,256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of Pixels')

# Equalized image and histogram
plt.subplot(2,2,3)
plt.imshow(eq, cmap='gray')
plt.title('Equalized Image')
plt.axis('off')

plt.subplot(2,2,4)
plt.plot(hist_equalized, color='black')
plt.title('Equalized Histogram')
plt.xlim([0,256])
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of Pixels')

plt.tight_layout()
plt.show()
