import cv2
import numpy as np

# Load image
image = cv2.imread("gulkok.jpg")
orig  = image.copy()

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# --- WHITE ROOTS MASK ---
lower_white = np.array([0, 0, 160])
upper_white = np.array([180, 30, 255])
mask_white = cv2.inRange(hsv, lower_white, upper_white)

# --- GREEN STEM MASK ---
lower_green = np.array([30, 40, 40])
upper_green = np.array([85, 255, 255])
mask_green = cv2.inRange(hsv, lower_green, upper_green)

# Combine roots + stem
mask = cv2.bitwise_or(mask_white, mask_green)

# Clean noise
kernel = np.ones((7,7), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)

# Keep ONLY the largest object (roots + stem)
cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
largest = max(cnts, key=cv2.contourArea)

final_mask = np.zeros_like(mask)
cv2.drawContours(final_mask, [largest], -1, 255, -1)

# Apply mask
result = cv2.bitwise_and(orig, orig, mask=final_mask)

cv2.imshow("Original", orig)
cv2.imshow("Mask (Roots + Stem ONLY)", final_mask)
cv2.imshow("Output", result)
cv2.waitKey(0)
