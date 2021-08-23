from L3 import rescaleFrame
import cv2 as cv
import numpy as np

orignal_img = cv.imread("images/img-3.jpeg")
img = rescaleFrame(orignal_img,scale = 0.2)
blank = np.zeros(img.shape,dtype='uint8')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT )
canny = cv.Canny(blur,125,175)

# contours 
contours, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

# find countours using threshhold
ret, thres = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
cv.imshow("Threshhold counter image", thres)

# draw contours
# cv.drawContours(blank,contours -1, (0,0,255), 2) # this is giving error dont not why


cv.waitKey(0)