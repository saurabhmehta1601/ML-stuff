# Bitwise operators in opencv
import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype="uint8")
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255 , -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow("Rectangle image", rectangle)
cv.imshow("Circle image", circle)


# Bitwise AND
bitwise_and = cv.bitwise_and(circle,rectangle ) # A intersecion B
cv.imshow("Bitwise and", bitwise_and)

# Bitwise OR
bitwise_or = cv.bitwise_or(circle,rectangle ) # A union B
cv.imshow("Bitwise or", bitwise_or)

# Bitwise xor
bitwise_xor = cv.bitwise_xor(circle,rectangle ) #  A - B union B - A
cv.imshow("Bitwise xor", bitwise_xor)

# Bitwise not
bitwise_not = cv.bitwise_not(rectangle ) # ~ A 
cv.imshow("Bitwise not", bitwise_not)

cv.waitKey(0)