import numpy as np
from L3 import rescaleFrame
import cv2 as cv

# translation image

def translate(img, x,y) : 
    transMat = np.float32([[1,0,x],[0,1,y]]) 
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMat, dimensions)

# rotate image

def rotate(img,angle,rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint == None :
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)




if __name__ =="__main__":
    orignal_img = cv.imread("images/img-1.jpg")
    img = rescaleFrame(orignal_img,scale = 0.2)

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
    dilated = cv.dilate(canny_blur, (7,7),iterations=3 )
    # cv.imshow("Dilated image", dilated)

    # eroding image
    eroded = cv.erode(dilated, (3,3), iterations =1)
    # cv.imshow("Eroded image", dilated)

    # resize image
    resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
    # cv.imshow("Resized image",resized)

    # cropping
    cropped = img[ 50:200, 200:400]
    # cv.imshow("Cropped image",cropped)
    
    # translate image
    translated = translate(img, 100 , 100)
    # cv.imshow("Translated image", translated)
    
    # rotate image
    rotated = rotate(img , 45) # -ve angle will rotate clockwise
    # cv.imshow("Rotated image", rotated)

    # flip image
    flip_h= cv.flip(img , 0) 
    flip_v= cv.flip(img , 1) 
    flip_vn= cv.flip(img , -1) 
    # cv.imshow("Resized image", flip_vn)

    cv.waitKey(0)
