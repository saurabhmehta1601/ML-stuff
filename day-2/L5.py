from L3 import rescaleFrame
import cv2 as cv

orignal_img = cv.imread("images/img-2.jpeg")
img = rescaleFrame(orignal_img,scale = 0.4)

# convert image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Grayscale Image ",gray)

# Blur image
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow("Blurred image", blur)

# Edge cascade (edges can be reduced by passing blur image)
canny_img = cv.Canny(img, 125,175)
canny_blur= cv.Canny(blur, 125,175)
# cv.imshow("Edge detected image", canny_img)
# cv.imshow("Edge detected blurred image", canny_blur)

# Dialting image




cv.waitKey(0)