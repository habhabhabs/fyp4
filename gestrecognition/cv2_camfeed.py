import numpy as np # dependency needed for opencv
import cv2 # opencv engine

cam = cv2.VideoCapture(0) # define camera connected to host 
cam.set(3, 320) # set horizontal size of camera
cam.set(4, 240) # set vertical size of camera

while True:
    b, img = cam.read()
    if b:
        cv2.imshow("Window", img)
    else:
        print("The camera is not working!")
        break
    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()
cam.release()
