import picamera
from time import sleep
camera=picamera.PiCamera()
Camera_resolution=(1024,768)
camera.brightness=60
camera.start_preview()
camera.annotate_text='Hi Pi User'
sleep(5)
camera.capture('/home/pi/IOT_practicals/Practicals/images/img2.jpeg')
camera.stop_preview()