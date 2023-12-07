# H : 0 - 190 
# S : 0 - 255
# V : 0 -

import cv2
import imutils
import numpy as np
print("Read library")

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    ret, frame = cap.read(0)
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #----- YELLOW -----
    yellow_osc = np.array([25, 70, 120])
    yellow_cla = np.array([30,255, 255])

    #-----  RED -----
    red_osc = np.array([0, 50, 120])
    red_cla = np.array([10, 255, 255])

    #----- GREEN -----
    green_osc = np.array([40, 70, 80])
    green_cla = np.array([70, 255, 255])

    #----- BLUE -----
    blue_osc = np.array([100, 70, 10])
    blue_cla = np.array([121 , 255, 255])

    #---- Pink ------
    pink_osc = np.array([1,1,1])
    pink_cla = np.array([1,1,1])

    cara1 = cv2.inRange(hsv,yellow_osc,yellow_cla)
    cara2 = cv2.inRange(hsv,red_osc,red_cla)
    cara3 = cv2.inRange(hsv,green_osc,green_cla)
    cara4 = cv2.inRange(hsv,blue_osc,blue_cla)
    cara5 = cv2.inRange(hsv,pink_osc,pink_cla)



    cnts1 = cv2.findContours(cara1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts1 = imutils.grab_contours(cnts1)

    cnts2 = cv2.findContours(cara2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts2 = imutils.grab_contours(cnts2)
    
    cnts3 = cv2.findContours(cara3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts3 = imutils.grab_contours(cnts3)

    cnts4 = cv2.findContours(cara4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts4 = imutils.grab_contours(cnts4)

    cnts5 =cv2.findContours(cara5, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts5 = imutils.grab_contours(cnts5) 


    for c in cnts1:
        area1 = cv2.contourArea(c)
        if area1 > 5000:
            cv2.drawContours(frame,[c], -1 ,(30, 255, 255),3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
            cv2.putText(frame, "YELLOW", (cx-20,cy-20),cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0),2)
            print("Color detection: yellow")

    for c in cnts2:
        area2 = cv2.contourArea(c)
        if area2 > 5000:
            cv2.drawContours(frame,[c], -1 ,(0, 0, 255),3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
            cv2.putText(frame, "RED", (cx-20,cy-20),cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0),2)
            print("Color detection: red")

    for c in cnts3:
        area3 = cv2.contourArea(c)
        if area3 > 5000:
            cv2.drawContours(frame,[c], -1 ,(0, 255, 0),3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
            cv2.putText(frame, "VERDE", (cx-20,cy-20),cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0),2)
            print("Color detection: green")

    for c in cnts4:
        area4 = cv2.contourArea(c)
        if area4 > 5000:
            cv2.drawContours(frame,[c], -1 ,(255, 0, 0),3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
            cv2.putText(frame, "BLUE", (cx-20,cy-20),cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0),2)
            print("Color detection: blue")
        '''
    for c in cnts5:
        area5 = cv2.contourArea(c)
        if area5 > 5000:
           #cv2.drawContours(frame,[c], -1 ,(255, 0, 0),3)
            M = cv2.moments(c)
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx,cy), 7, (255,255,255), -1)
            cv2.putText(frame, "PINK", (cx-20,cy-20),cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0),2)
            print("Color detection: pink")
'''
    cv2.imshow('Video', frame)
    k = cv2.waitKey(1)
    if k == 32:
        break

cap.release()
cv2.destroyAllWindows()

