#! /usr/bin/python
import cv2
import time

cap=cv2.VideoCapture(0)

while cap.isOpened():
	#print "camera is working"
	status,frame=cap.read()
	onlyred=cv2.inRange(frame,(0,0,0),(30,30,255))
	cv2.imshow("red",onlyred)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cv2.destroyAllWindows()
cap.release()


