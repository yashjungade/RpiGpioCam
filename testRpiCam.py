import cv2
from picamera import PiCamera
import time
from picamera.array import PiRGBArray
camera=PiCamera()
camera.resolution=(640,480)
camera.framerate=32
rawCapture=PiRGBArray(camera, size=(640,480))
time.sleep(0.1)
for frame in camera.capture_continuous(
    rawCapture, format='bgr', use_video_port=True):
    img=frame.array
    cv2.imshow('Camera', img)
    c = cv2.waitKey(1)
    rawCapture.truncate(0)
    if c == 27 or c == 10:
        cv2.destroyAllWindows()
        break
