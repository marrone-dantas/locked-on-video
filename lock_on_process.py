import cv2
from util import *
import sys
import face_recognition


def extract_frames(path_video,path_output,sufix="frame_"):

	cap= cv2.VideoCapture(path_video)
	i=0
	while(cap.isOpened()):
		ret, frame = cap.read()
		if ret == False:
			break
		cv2.imwrite(path_output+'/'+sufix+"_"+str(i)+'.png',frame)
		i+=1
		print('\r' + str(i)+" frames extracteds!", end='')


	cap.release()
	cv2.destroyAllWindows()
	print("\n->Extraction finished!")

def create_video(path_input,output_video,fps=30):

	files_names = get_filepaths(path_input)

	mg = cv2.imread(files_names[0])

	shape_mg = int(mg.shape[1]),int(mg.shape[0])

	out = cv2.VideoWriter(output_video,
	cv2.VideoWriter_fourcc(*"MJPG"), fps ,shape_mg)


	for i in range(0,len(files_names),1):

		print('\r' + str(i)+" frames to video!", end='')
		img = cv2.imread(files_names[i])
		img=cv2.resize(img,shape_mg)
		out.write(np.uint8(img))

	out.release()

def detect_faces(folder_path,croped_path,rate,x_scale=200,y_scale=100):

	frames_paths = get_filepaths(folder_path)

	positions = None

	fixed_position = None
	initial_position = None

	for idx in range(0,len(frames_paths),1):
		
		print('\r' + "Faces detected: "+str(idx+1)+" from "+str(len(frames_paths)), end='')

		img = cv2.imread(frames_paths[idx])

		original_w = img.shape[0]
		original_h = img.shape[1]

		new_w = int(original_w/rate)
		new_h = int(original_h/rate)

		img = cv2.resize(img,(new_h,new_w))

		rgb_small_frame = img[:, :, ::-1]

		frame = cv2.imread(frames_paths[idx])
		face_locations = face_recognition.face_locations(rgb_small_frame)

		if (len(face_locations)!=0):

			positions = face_locations[0]

		top, right, bottom, left = positions
		top = int(top*rate)
		right =int(right*rate)
		botton = int(bottom*rate)
		left =int(left*rate)
		
		center = (left+int((right-left)/2),top+int((botton-top)/2))
		
		if (fixed_position is None):
			
			fixed_position = center
		
		if (initial_position is None):
			
			initial_position = positions
			
		diff = fixed_position[0] - center[0],fixed_position[1] - center[1]
		
		num_rows, num_cols = frame.shape[:2]

		translation_matrix = np.float32([ [1,0,diff[0]], [0,1,diff[1]] ])
		img_translation = cv2.warpAffine(frame, translation_matrix, (num_cols, num_rows))
		
		top, right, bottom, left = initial_position
		top = int(top*rate)
		right =int(right*rate)
		botton = int(bottom*rate)
		left =int(left*rate)
		
		crop = img_translation[top-x_scale:top+int((botton-top)+x_scale),left-y_scale:left+int((right-left))+y_scale]
		
		cv2.imwrite(croped_path+"/output_"+str(idx)+".png",crop)
	print("\n->Detection finished")
	