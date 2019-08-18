
from addFace import addingFace
import cv2 
from surv import survey


known_faces_encoding = []
known_faces_name = []

while True:
	### main menu
	print("Main Menu : ")
	print("1 - Start Surveillance")
	print("2 - Add a Face")
	print("3 - Remove a Face")
	print("4 - Show All Owners")
	print("5 - EXIT")
	ans = int(input("Your Response : "))

	### surveillance 
	if ans == 1:
		survey(known_faces_encoding,known_faces_name)


	### Adding a face
	elif ans == 2:
		new_face_encoding,newName = addingFace()

		known_faces_encoding.append(new_face_encoding)
		known_faces_name.append(newName)
	


	### Remove a face
	elif ans == 3:
		print("!!!!! BOOM !!!!! Face Removed (haven't coded yet)")

	### Displaying all owners
	elif ans == 4:
		if not known_faces_name:
			print("NO Owners Yet")
		else:	
			for x in known_faces_name:
				print(x)	


	### EXIT	
	elif ans == 5:
		print("FINISHED")
		break


	### Inlvalid input	
	else :
		print("Enter Valid Input")	

	print("Press any key to continue")	
	while True:
		wait = input("")
		if wait:
			break

	continue	 