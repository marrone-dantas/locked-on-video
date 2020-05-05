#!/usr/bin/python
from lock_on_process import *
import argparse
import shutil
import os

#
#fps = get_video_fps("demo6.mp4")
#detect_faces("frames","croped",2,x_scale=200,y_scale=100)
#extract_audio("demo6.mp4","crop.mp3")
#create_video("croped","crop.mp4",fps=fps)
#combine_audio("crop.mp4", "crop.mp3", "mix.mp4",fps=fps)



import sys, getopt

def run(argv):
	
	return None

if __name__ == "__main__":

	#Load variables
	parser = argparse.ArgumentParser(description='Run lock-on on single videl.')
	parser.add_argument('video_input', type=str, help='a input video to run the lock-on')
	parser.add_argument('output_video', type=str, help='a output video path')
	parser.add_argument('x_scale', type=int, help='x scale to expand')
	parser.add_argument('y_scale', type=int, help='y scale to expand')
	parser.add_argument('rate', type=int, help='rate to resize to')

	args = parser.parse_args()
	
	#Remove previous data
	try:

		shutil.rmtree('frames')
		shutil.rmtree('croped')

	except:

		print("Folders already removed")

	#Create new folder
	create_folder("frames")
	create_folder("croped")

	#Extract frames
	extract_frames(args.video_input,"frames",sufix="frame_")

	#Get video fpd
	fps = get_video_fps(args.video_input)

	#Detect the faces on the image
	detect_faces("frames","croped",args.rate,x_scale=args.x_scale,y_scale=args.y_scale)

	#Extract audio from original video
	extract_audio(args.video_input,"temp.mp3")

	#Generate video from frames
	create_video("croped","crop.mp4",fps=fps)

	#Join video and audio
	combine_audio("crop.mp4", "temp.mp3", args.output_video,fps=fps)

	#Remove temp files
	try:

		shutil.rmtree('frames')
		shutil.rmtree('croped')

	except:

		print("Folders already removed")

	os.remove("crop.mp4")
	os.remove("temp.mp3")


