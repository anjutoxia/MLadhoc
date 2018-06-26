#! /usr/bin/python
import cv2
import time
'''
def diffinframes(x,y,z):
	img1=cv2.absdiff(x,y)
	img2=cv2.absdiff(y,z)
	comm_diff=cv2.bitwise_and(img1,img2)
	return comm_diff
'''
#enabling camera
cap=cv2.VideoCapture(0)

#capturing 3 consistent frames
frame1=cap.read()[1]
frame2=cap.read()[1]
frame3=cap.read()[1]

#converting to grayscale
gray1=cv2.cvtColor(frame1,0)
gray2=cv2.cvtColor(frame2,0)
gray3=cv2.cvtColor(frame3,0)

while cap.isOpened():
	img1=cv2.absdiff(gray1,gray2)
	img2=cv2.absdiff(gray2,gray3)
	comm_diff=cv2.bitwise_and(img1,img2)
	#show motion detected frames
	cv2.imshow("camera",comm_diff)
	#capture more frames for further processing
	status,frame=cap.read()
	gray1=gray2
	gray2=gray3
	gray3=cv2.cvtColor(frame,0)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
