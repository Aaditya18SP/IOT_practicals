import picamera
import time
#from time import sleep

#create object of PiCameras
camera=picamera.PiCamera()

#set resolution
camera.resolution=(1024,768)
camera.brightness = 60
camera.start_preview()

#add text on image
camera.annotate_text ='Hi Pi User'
time.sleep(10)

#store image . You can mention the path
camera.capture('/home/pi/IOT_practicals/Practicals/images/image1.jpeg')
camera.stop_preview()

