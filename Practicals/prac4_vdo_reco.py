import picamera
import time
 
 #create object
camera=picamera.PiCamera()

#set the resolutio¬n
camera.resolution=  (640,480)

#start the recording in .h264 format only -> mention the path as well
camera.start_recording("/home/pi/IOT_practicals/Practicals/video/demo.h264")

#wait for the recording to finish
camera.wait_recording(10)

#finish recording
camera.stop_recording()

#close the camera
camera.close()

#to indicate to the user that the recording has stopped
print("video recording stopped")

#sudo omxplayer videoname to play the video