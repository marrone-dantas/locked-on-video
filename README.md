# Locked-on-video

The locked-on is a simple implementation of the face lock-on in python. Face lock-on is a type of stabilization, but in this case, we keep the face static. 

A famous application of this type of technique was used on the [Beats By Dre](https://www.youtube.com/watch?v=Dd1VIeTMGQs). The inspiration for this project came from the tutorial with after-effects on the [Cinecom youtube channel](https://www.youtube.com/watch?v=Z2dTgRbN-3E).  We can get much better results doing the process manually, but here we try to make **automatic** and **free**. 


>Disclaimer: Notice that this project was done with the purpose of **study** and **practice**. Need a set of optimization and tweaks. 

Bellow, we can san an example, the input video contains a girl dancing on the left, and as output, we get just the video on her face fixed on the right.

<p align="center">

  <img  src="joined.gif">

</p>

We get each video and extract all the frames; on each frame, we detect the faces. With the faces detect, we set the center of the faces and calculate the variance between consecutive frames.  With the variance, we translate the images to the original center (the position the face on the first frame). Since we translate the image, we can get an image border, so to get a clear image, we crop the video.

# Requiriments

The code was tested on python 3.6. The requirements can be installed by the `requiriments.txt` with `pip install -r requiriments.txt`. Bellow, we can see the requirements.

 - `opencv-python==4.2.0.32`
 - `face-recognition==1.3.0`
 - `face-recognition-models==0.3.0`
 - `numpy==1.18.1`
 - `moviepy==1.0.2`

# Usage

The usage is pretty simple; you only need a video as input and run the script below.

`python run_lock.py video_input_path video_output_path x_scale y_scale rate`

The parameters are described bellow:

 - `video_input_path`: the video to be processed
 - `video_output_path`: the output video
 - `x_scale`and `y_scale`: this parameter controls the border expands around the face detected if we want a bigger area around the face; we can tune this parameter.
 - `rate`: since we run the detection on each frame, sometimes it can be time-consuming, this rate reduces the image size to detection. For instance, a `rate==2` reduces the image input dimension by half. If the rate is to low, maybe the detection does not work.
 
# Known issues

 - [ ] The video needs to be clean and with a good resolution. 
 - [ ] Work with one person at a time.
 - [ ] It can take some time with large videos.
 - [ ] Change the detections for object tracking.
 
>I want to thank the [face_recognition](https://github.com/ageitgey/face_recognition); this project mainly uses the tools provided by **face_recognition**. 
