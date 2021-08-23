# Masking

import cv2 as cv
import numpy as np
from L3 import rescaleFrame

img = rescaleFrame(cv.imread('images/img-3.jpeg'),0.3)
blank = np.zeros(img.shape[:2], dtype="uint8")

cv.imshow("Image", img)
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255,-1)
cv.imshow("Mask", mask)

masked = cv.bitwise_and(img, img , mask= mask)
masked = cv.line(masked, (masked.shape[1]//2,0), (masked.shape[1]//2, masked.shape[0]), 0, 2)
masked = cv.line(masked, (0,masked.shape[0]//2), ( masked.shape[0],masked.shape[0]//2), 0, 2)

cv.imshow("Masked Image", masked)

cv.waitKey(0)