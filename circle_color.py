import numpy as np
import cv2

canvas = np.zeros((2000, 2000, 3), dtype = "uint8")
for i in range(0, 10000):
    radius = np.random.randint(5, high = 500)
    color = np.random.randint(0, high = 256, size = (3,)).tolist()
    pt = np.random.randint(0, high = 2000, size = (2,))
    cv2.circle(canvas, tuple(pt), radius, color)
(b, g, r) = canvas[0, 0]

canvas[0, 500] = (0, 0, 255)
canvas[500, 500] = (0, 0, 255)
canvas[500, 500] = (0, 0, 255)
canvas[0, 500] = (0, 0, 255)
canvas[0, 500] = (0, 0, 255)

canvas[500, 500] = (0, 0, 255)
canvas[2, 500] = (0, 0, 255)
canvas[1500, 500] = (0, 0, 255)

(b, g, r) = canvas[0, 0]
cv2.imshow("Canvas",canvas)
cv2.waitKey(0)

