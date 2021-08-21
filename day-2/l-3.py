# Resizing and rescaling frames
import cv2 as cv

def changeResolution(width,height):
    # works for live video only use rescaleFrame for already existing file
    capture.set(3,width) 
    capture.set(4,height)


# for rescaling image frames (video is array of frames)
def rescaleFrame(frame , scale= 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions =  (width, height)
    return cv.resize(frame, dimensions , interpolation = cv.INTER_AREA)

capture = cv.VideoCapture("videos/vid-1.mp4")

while True: 
    isTrue,frame = capture.read()
    resized_frame = rescaleFrame(frame)
    resized_frame_smaller = rescaleFrame(frame,scale=0.2)
    resized_frame_bigger = rescaleFrame(frame,scale=2)
    cv.imshow("Resized video frame", resized_frame)
    cv.imshow("Resized video frame even smaller ", resized_frame_smaller)
    cv.imshow("Resized video frame", resized_frame_bigger)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()