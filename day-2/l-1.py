# Read an image
import cv2 as cv

img = cv.imread("images/img-1.jpg")
cv.imshow("My image window", img)
cv.waitKey(0)