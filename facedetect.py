'''to detect faces in video capturing mode
import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)
while True:
	_, img=cap.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(gray,1.1,4)
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

	cv2.imshow('img',img)
	k=cv2.waitKey(30) & 0xff
	if k==27:
		break

cap.release()'''
#to detect faces in images
'''
import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img=cv2.imread('testimg.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1,4)
for(x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey()
'''