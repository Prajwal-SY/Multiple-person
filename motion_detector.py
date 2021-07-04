
import cv2
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  
cap= cv2.VideoCapture(0)
buzzer=2

GPIO.setup(buzzer,GPIO.OUT)

GPIO.output(buzzer,False)

GPIO.setmode(GPIO.BCM)  

while True:
## Detecting no. of faces in the frames .
        face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        
        font = cv2.FONT_HERSHEY_SIMPLEX
##        while True:

        ret, image_frame = cap.read()
        gray = cv2.cvtColor(image_frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:

            # Crop the image frame into rectangle
            cv2.rectangle(image_frame, (x,y), (x+w,y+h), (255,0,0), 2)
                       # Display the video frame, with bounded rectangle on the person's face
            if (len(faces)) > 2 :
                print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Found more than two persons in ATM>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                print("2 person detected")
                cv2.imwrite('frame.jpg',image_frame)
                GPIO.output(buzzer,True)
                time.sleep(2)
                GPIO.output(buzzer,False)
                time.sleep(2)

            cv2.putText(image_frame,'Number of Faces : ' + str(len(faces)),(40, 40), font, 1,(255,0,0),2)
        cv2.imshow('frame', image_frame)
        
        # To stop taking video, press 'q' for at least 100ms
        if cv2.waitKey(100) & 0xFF == ord('l'):
            break

camera.release()
cv2.destroyAllWindows()
