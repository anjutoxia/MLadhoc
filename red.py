#! /usr/bin/python
import cv2,time
#read the image
img=cv2.imread('/home/anju/Desktop/red.jpg')
grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#shape of the image
print img.shape
time.sleep(3)
#printing data
print img
print grayimg

time.sleep(5)
#extracting red color

onlyred=cv2.inRange(img,(0,0,0),(50,50,255))
cv2.imshow('original',img)
cv2.imshow('gray',grayimg)
cv2.imshow('onlyred',onlyred)
cv2.imwrite('blackbutterfly.jpeg',onlyred)
cv2.waitKey(0)
cv2.destroyAllWindows()
i
