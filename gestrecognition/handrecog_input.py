import cv2
import numpy as np
import math
from pynput.keyboard import Key, Controller
import time
import sys
from pywinauto.keyboard import SendKeys

print("Starting gesture recognition engine...")
print("Platform detected: " + sys.platform)
cam = cv2.VideoCapture(0)
keyboard = Controller()
bufferLock: bool = False
 
while True:
    try:  
        # define camera settings
        ret, frame = cam.read()
        frame = cv2.flip(frame, 1)
        kernel = np.ones((3, 3), np.uint8)
        
        # define region of interest (detection area)
        roi = frame[100:300, 100:300]
        cv2.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
         
        # define range of skin colour in HSV (Hue Saturation Values) 
        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
        lower_skin = np.array([0, 20, 70], dtype = np.uint8)
        upper_skin = np.array([20, 255, 255], dtype = np.uint8)
        
        # check if skin colour defined matches lower_skin and upper_skin bounds  
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        
        # filling dark spots by extrapolating the hand's image
        mask = cv2.dilate(mask, kernel, iterations = 4)
        
        # use gaussian blur to enhance detection and binary conversion of image
        mask = cv2.GaussianBlur(mask, (5, 5), 100) 
        
        # identifying the contours of hand
        _, contours, hierarchy= cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
        # find maximum area for hand contour
        cnt = max(contours, key = lambda x: cv2.contourArea(x))
        
        # provide close approximation of contour
        epsilon = 0.0005 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
    
        # generate a convex hull surrounding the hand
        hull = cv2.convexHull(cnt)
        
        # create the contours of hull and surrounding of hand
        areahull = cv2.contourArea(hull)
        areacnt = cv2.contourArea(cnt)
    
        # calculate % of area not covered by hand in convex hull
        arearatio = ((areahull - areacnt) / areacnt) * 100
    
        # identify all the defects in convex hull (lowest points between fingers, aka gap)
        hull = cv2.convexHull(approx, returnPoints = False)
        defects = cv2.convexityDefects(approx, hull)
        
        # l = no. of defects (gap between two fingers)
        l = 0
        
        # code for finding no. of defects (gaps between fingers) after identifying
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0]
            start = tuple(approx[s][0])
            end = tuple(approx[e][0])
            far = tuple(approx[f][0])
            pt = (100, 180)
            
            # find length of all sides of triangle (three points: finger 1, finger 2, defect)
            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            s = (a + b + c) / 2
            ar = math.sqrt(s * (s - a) * (s - b) * (s - c))
            
            # distance between point and convex hull
            d = (2 * ar) / a
            
            # calculate the angle of the defect using cosine
            angle = math.acos((b ** 2 + c ** 2 - a ** 2)/(2 * b * c)) * 57
            
            # ignore angles > 90 and ignore points very close to convex hull (they generally come due to noise)
            if angle <= 90 and d > 30:
                l += 1
                cv2.circle(roi, far, 3, [255, 0, 0], -1)
            
            # draw lines around hand
            cv2.line(roi,start, end, [0, 255, 0], 2)
            
        # formula for number of fingers: defects + 1    
        l += 1
        
        # print corresponding gestures which are in their ranges
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # if there are five fingers in detection region
        if l == 5:
            cv2.putText(frame, 'Talk now', (150, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
            # Press and release space
            time.sleep(1)
            
            # start of keypress simulation
            if bufferLock is False:
                bufferLock = True
            
            if sys.platform == "win32":
                SendKeys("                                                                                                                                          ", with_spaces=True)
            else:
                keyboard.press(Key.space)
                t: int = 6
                while t > 0:
                    mins, secs = divmod(t, 60)
                    timeformat = '{:02d}:{:02d}'.format(mins, secs)
                    print(("Holding space bar for: " + timeformat), end = '\r')
                    time.sleep(1)
                    t -= 1
                if t == 0 and sys.platform == "win32":
                    keyboard.release(Key.space)
                time.sleep(1)

            # completion of execution
            if bufferLock is True:
                t: int = 4
                while t > 0:
                    mins, secs = divmod(t, 60)
                    timeformat = '{:02d}:{:02d}'.format(mins, secs)
                    print(("Timeout before next press: " + timeformat), end = '\r')
                    time.sleep(1)
                    t -= 1
                bufferLock = False


        else :
            cv2.putText(frame, 'Wave hand', (150, 50), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
            
        #show the windows
        cv2.imshow('Mask', mask)
        cv2.imshow('Detection Frame', frame)

    except:
        pass
        
    # if hit escape key, exit program
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break
    
cv2.destroyAllWindows()
cam.release()    

                                                                                                                                                                                                                                                                                          
