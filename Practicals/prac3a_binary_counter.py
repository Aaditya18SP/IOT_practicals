import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
bina_hex= ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
'''bina_oct = ['000','001','010','011','100','101','110','111']'''
'''bina_oct.len'''
for i in range(0,8):
    current=bina_hex[i]
    GPIO.output(11,int (current[0]))
    GPIO.output(13,int(current[1]))
    GPIO.output(15,int(current[2]))
    GPIO.output(12,int(current[3]))
    time.sleep(2)
    '''GPIO.output(12,(int)current[3])'''
    
    