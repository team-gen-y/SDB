import face_recognition 
import cv2
import numpy as np
from sms import send_sms

def survey(known_face_encoding,know_face_names):
	
	cap = cv2.VideoCapture(0)
	process_this_fame = True
	#sms_notfi = True
	k=0
	final_name = []
	ite = 0 
	while True:
		ret , frame = cap.read()
		small_frame = cv2.resize(frame,(0,0), fx = 0.25 , fy = 0.25)
		rgb_small_frame = small_frame[:,:,::-1]

		if process_this_fame:
			face_locations = face_recognition.face_locations(rgb_small_frame)
			face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
			face_names = []
			
			for face_encoding in face_encodings:
				matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
				name = "Unknown"

				face_distances = face_recognition.face_distance(known_face_encoding,face_encoding)
				best_match_index = np.argmin(face_distances)
				if matches[best_match_index]:
					name = know_face_names[best_match_index]

				face_names.append(name)			
				#print(face_names)
				length = len(face_names)
				ite = ite + 1
				print(ite)
				if length > k :
					k = length
					final_name = face_names
				if ite == 20 :
					#print(final_name)
					heavy_text = ""
					for stuff in final_name:
						heavy_text = heavy_text + stuff + " "
					heavy_text = heavy_text + "at your door"	
					print(heavy_text)
					#send_sms(heavy_text)



		process_this_fame = not process_this_fame

		### displaying your result	
				#display()