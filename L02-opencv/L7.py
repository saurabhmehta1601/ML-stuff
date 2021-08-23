#  color spilitting
import cv2 as cv
import numpy as np

img = cv.imread('images/img-4.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')

cv.imshow("Image original",img)

blue,green,red = cv.split(img)
cv.imshow("Red image", red) # ligher parts are where red is max
cv.imshow("blue image", blue) # ligher parts are where blue is max
cv.imshow("green image" , green) # ligher parts are where green is max

blue_img= cv.merge([blue,blank,blank]) # passing blue array for blue 
green_img = cv.merge([blank,green,blank]) # passing green array for blue 
red_img = cv.merge([blank,blank,red]) # passing red array for blue 

cv.imshow("image red",red_img)
cv.imshow("image blue",blue_img)
cv.imshow("image green",green_img)

cv.waitKey(0)