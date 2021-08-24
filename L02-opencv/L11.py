import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from L3 import rescaleFrame
import matplotlib.pyplot as plt

img = rescaleFrame(cv.imread('images/img-3.jpeg'),0.3)
blank = np.zeros(img.shape[:2], dtype="uint8")

gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)

# without mask 
gray_hist = cv.calcHist([gray], [0], None, [256],[0,256])
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# No of pixels")

plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# with mask 
mask= cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1 ) 
masked = cv.bitwise_and(gray ,gray, mask= mask)

gray_hist = cv.calcHist([gray], [0], mask, [256],[0,256])
plt.figure()
plt.title("Grayscale Histogram with mask ")
plt.xlabel("Bins")
plt.ylabel("# No of pixels")

plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

colors = ("b", "g", "r")

for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.title("color histogram")
plt.show()
cv.imshow("Mask ", mask)
cv.waitKey(0)
