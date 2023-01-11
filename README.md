# AI-Project
A respository for the Semester Project of my AI Course.
## Introduction
This repository is an implementation of the posture detection AI Model created by mediapipe, and captures the media video using OpenCV. Initially, the webcame is selected, but if you wish to change it and try it on another media, you can do so, refer to the "Change media" section below. This Project uses angles between the joints of limbs to track rep progress of exercises. So far, only 2 exercises were implemented since this was a semester Project. There is also a Rep counter that shows the amount of full ROM reps you've done.
## Bicep Curls Trainer
It finds the angles between your shoulder and elbows, then elbows and your wrist, to make sure that the whole range of motion is being done. In order to see best results, try standing sideways, however it was tuned to work even when you're facing the camera. 
## Squats Trainer
Similarly, it finds the angle between your hip bone, your knees, and also your knees to your feet, and then shows you the amount of progress based on range of motion you're doing. Standing sideways or upfront doesn't really make a difference to this, however do make sure that the camera is not too high up.
### Change Media
To change the video to and external media or a file saved on your pc, you need to change the "0" in "cv2.VideoCapture()" to anything, inside the Trainer Files:
cv2.VideoCapture("path/to/file")
This change needs to be made in whichever Trainer you're using.