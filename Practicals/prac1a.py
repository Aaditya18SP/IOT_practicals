import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)
while(1):
    GPIO.output(13,1)
    time.sleep(1)
    GPIO.output(13,0)
    time.sleep(1)
    
