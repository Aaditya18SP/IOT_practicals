import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

'''bina_oct.len'''
def dec_to_bin(num):
    binary_num=""
    while(num > 0):
        binary_num += str(num%2)
        num=num/2
        
    binary_num+=str(num)
    return binary_num
    
for i in range(0,8):
    current=dec_to_bin(i)
    print(current)
    GPIO.output(11,int (current[0]))
    '''GPIO.output(13,int(current[1]))
    GPIO.output(15,int(current[2]))
    time.sleep(2)'''
    '''GPIO.output(12,(int)current[3])'''
    
    
