#! /usr/bin/python
import cv2
#print dir(cv2)
#reading image
#image name, image features
#we can write cv2.IMREAD_COLOR instead of 1
img=cv2.imread('index.jpeg',1)
img1=cv2.imread('index.jpeg',0)
cv2.imshow('cat',img)
cv2.imshow('cat1',img1)
cv2.waitkey(0)

