import face_recognition
import cv2
import csv

def addingFace():
	newName = input("Enter Name : ")
	cap = cv2.VideoCapture(0)
	while True:
		ret , face = cap.read()
		cv2.imwrite('V:/Personal Documentation/Smart door/env1/owners/Face/'+newName+'\'s ' +'Image.jpg',face)
		face_encoding = face_recognition.face_encodings(face)[0]
		#print(face_encoding)		
		#with open('ownerFaceEncoding.csv','a') as fd:
    	#	fd.write(face_encoding)
		break
	return face_encoding,newName 		
	cap.release()
	cv2.destroyAllWindows()	
		
