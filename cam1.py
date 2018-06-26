#!/usr/bin/python2
import cv2
import random
cap=cv2.VideoCapture(0)
while cap.isOpened():
	print "camera is working"
	status,frame=cap.read()
	bwimg=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
	cv2.rectangle(frame,(100,100),(200,200),(255,0,0),3)
	cv2.rectangle(frame,(100,250),(200,350),(255,0,0),3)
	cv2.rectangle(frame,(300,100),(400,200),(255,0,0),3)
	cv2.rectangle(frame,(300,250),(400,350),(255,0,0),3)
	cv2.imshow("camera1",frame)
	cv2.imshow('camera2',bwimg)
	x=random.random()
	y=str(x)[2:5]
	cv2.imwrite("anju"+y+".jpg",frame)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
cv2.destroyAllWindows()
cap.release()	
