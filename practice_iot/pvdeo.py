import picamera
from time import sleep
camera=picamera.PiCamera()
camera.resolution=(640,320)
camera.start_recording('/home/pi/IOT_practicals/Practicals/video/vdeo2.h264')
camera.wait_recording(5)
camera.stop_recording()
camera.close()
print('stop')