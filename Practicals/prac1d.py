import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
bina = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
for i in range(0,bina.length):
    current=bina[i]
    GPIO.output(11,current[0])
    GPIO.output(13,current[1])
    GPIO.output(15,current[2])
    GPIO.output(12,current[3])
    
    