import cv2
from time import sleep

camera = cv2.VideoCapture(0)

while True:
	status, image = camera.read()
	if(status):
		cv2.imshow("Videog",image)
		if cv2.waitKey(10) == ord('q'):
			break
	sleep(.01) 
	
	
