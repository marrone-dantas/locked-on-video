import cv2
import os
import re
import numpy as np
import sys
import moviepy.editor as mp
import moviepy.editor as mpe
import time

def create_folder(path):

	try:
		os.mkdir(path)
	except OSError:
		print ("Creation of the directory %s failed" % path)
	else:
		print ("Successfully created the directory %s " % path)

def get_video_fps(video_input):

	video = cv2.VideoCapture(video_input);
	fps = video.get(cv2.CAP_PROP_FPS)
	video.release()

	return fps

def clean_print(string):
	sys.stdout.write(string)
	sys.stdout.flush()

def extract_audio(video_input,audio_ouput):

	clip = mp.VideoFileClip(video_input)
	clip.audio.write_audiofile(audio_ouput)

def combine_audio(vidname, audname, outname, fps=25):

	my_clip = mpe.VideoFileClip(vidname)
	audio_background = mpe.AudioFileClip(audname)
	final_clip = my_clip.set_audio(audio_background)
	final_clip.write_videofile(outname,fps=fps)	

def natural_sort(l): 
	convert = lambda text: int(text) if text.isdigit() else text.lower() 
	alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
	return sorted(l, key = alphanum_key)

def get_filepaths(directory):

	file_paths = []  

	for root, directories, files in os.walk(directory):
		for filename in files:
		
			filepath = os.path.join(root, filename)
			file_paths.append(filepath)  

	return natural_sort(file_paths) 