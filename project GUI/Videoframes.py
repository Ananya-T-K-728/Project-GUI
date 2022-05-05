import cv2 
import os 
video = cv2.VideoCapture(r'C:\Users\ananya\Desktop\project GUI\A 20 second video of Lake Louise.mp4') 
try:  
	if not os.path.exists('pet'): 
		os.makedirs('pet') 
except OSError: 
	print ('Error') 
currentframe = 0
while(True): 
	ret,frame = video.read() 

	if ret: 
		name = './pet/frame' + str(currentframe) + '.jpg'
		print ('Captured...' + name) 
		cv2.imwrite(name, frame) 
		currentframe += 1
	else: 
		break
video.release() 
cv2.destroyAllWindows()