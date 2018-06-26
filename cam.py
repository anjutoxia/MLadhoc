#! /usr/bin/python2
import cv2
#now starting cam
cap=cv2.VideoCapture(0)
while  cap.isOpened():
	print "camera is working"
	status,frame=cap.read()
	cv2.imshow("camera",frame)
	cv2.waitKey(1)
cv2.destroyWindow("camera")
cap.release 

