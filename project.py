import cv2
import numpy as np

# Load image
image = cv2.imread("gulkok.jpg")
orig = image.copy()

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# COLOR SEGMENTATION 
# Roots (white)
root_mask = cv2.inRange(hsv, (0, 0, 180), (180, 70, 255))

# Stem (green)
stem_mask = cv2.inRange(hsv, (25, 40, 40), (95, 255, 255))

# Combine root + stem
mask = cv2.bitwise_or(root_mask, stem_mask)

# REMOVE SMALL NOISE (CONNECTED COMPONENTS) 
num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(mask, connectivity=8)

clean_mask = np.zeros_like(mask)
min_area = 1500  # keeps roots, removes background noise

for i in range(1, num_labels):
    if stats[i, cv2.CC_STAT_AREA] > min_area:
        clean_mask[labels == i] = 255

#  VERY LIGHT SMOOTHING (PRESERVES ROOT SHAPE) 
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
clean_mask = cv2.morphologyEx(clean_mask, cv2.MORPH_CLOSE, kernel, iterations=1)

# REMOVE STEM FROM BINARY MASK (KEY FIX) 
roots_only_mask = cv2.bitwise_and(
    clean_mask,
    cv2.bitwise_not(stem_mask)
)

# REMOVE REMAINING WHITE BACKGROUND (KEEP ROOT CLUSTER ONLY)  “Non-root artifacts were eliminated by retaining only the largest connected component corresponding to the root system.”
num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(
    roots_only_mask, connectivity=8
)

# Create empty mask
roots_clean = np.zeros_like(roots_only_mask)

# Ignore background (label 0)
largest_label = 1 + np.argmax(stats[1:, cv2.CC_STAT_AREA])

# Keep only the largest connected component (the roots)
roots_clean[labels == largest_label] = 255



# ROOT AREA CALCULATION 
root_only_area_pixels = cv2.countNonZero(roots_clean)
print("Root-only area (pixels):", root_only_area_pixels)

# VISUALIZATION 
final = cv2.bitwise_and(orig, orig, mask=clean_mask)

# The area is reported in pixel units because no physical scale was provided so I used scale calibration.
# for example 1 pixel = 0.1 mm
pixel_size_mm = 0.1  # 1 pixel = 0.1 mm (assumed)

root_area_mm2 = root_only_area_pixels * (pixel_size_mm ** 2)

print("Root area (mm^2):", root_area_mm2)



cv2.imshow("Clean Mask (Root + Stem)", clean_mask)
cv2.imshow("Roots Only Mask", roots_only_mask)
cv2.imshow("Final Segmentation", final)

cv2.waitKey(0)
cv2.destroyAllWindows()
