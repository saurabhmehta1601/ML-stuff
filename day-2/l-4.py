# Draw and write on image
import cv2 as cv
import numpy as np

blank = np.zeros((500,500 ,3), dtype='uint8')

# blank[:] = 0,255,0
# cv.imshow("Green",blank)

# blank[:] = 255,0,0
# cv.imshow("Blue",blank)

# blank[:] = 0,0,255
# cv.imshow("Green",blank)

# cutting parts of images
# blank[200:300, 300:400] = 0,0,255
# cv.imshow("image window",blank)

# # Drawing a rectangle outline on screen
# cv.rectangle(blank, (50,50), (250,350), (255,0,0),thickness=2)
# cv.imshow("Rectangle window ", blank)

# # Drawing a rectangle filled on screen
# cv.rectangle(blank, (50,50), (250,350), (255,0,0),thickness=cv.FILLED) #thickness = -1 will be same
# cv.imshow("Rectangle window ", blank)

# Accessing coordinates from blank.shape which is tuple (height, width)
# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,0,0),thickness=-1) #thickness = -1 will be same
# cv.imshow("Rectangle window ", blank)

# Draw a circle
# cv.circle(blank,(250,250),50,(0,0,255),thickness=3)
# cv.imshow('Circle',blank)




cv.waitKey(0)