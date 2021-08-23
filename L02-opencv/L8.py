# smoothing and blurring
import cv2 as cv
import numpy as np

img = cv.imread('images/img-3.jpeg')
blank = np.zeros(img.shape[:2], dtype='uint8')

# Average blur  finds average of surrounding pixels in kernel window
blur_avg = cv.blur(img, (3,3))  
cv.imshow("Rounding Blur image ", blur_avg)

# Gaussian blur  based on weights 
blur_gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian Blur image ", blur_gauss)

# Median blur  finds median of surrounding pixels in kernel window
blur_median =  cv.medianBlur(img, 3)
cv.imshow("Median Blur image ", blur_median)

# Bilateral blurring 
blur_bilateral = cv.bilateralFilter(img, 10,  35, 25)
cv.imshow("Bilateral Blur image ", blur_bilateral)


cv.waitKey(0)