# reading a video 
import cv2 as cv

capture = cv.VideoCapture('videos/vid-1.mp4')

while True:
    isTrue,frame = capture.read()
    cv.imshow("My image window", frame)
    if cv.waitKey(20) & 0xFF == ord('d') :
        break

capture.release()
cv.destroyAllWindows