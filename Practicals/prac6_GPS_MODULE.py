import time
import serial
import string
import pynmea2
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
port ="/dev/ttyAMA0"
ser=serial.Serial(port,baudrate=9600,timeout=0.5)
while(1):
    try:
        data=ser.readline()
        print(data)
    except:
        print("loading")
    
    if(data[0:6] == '$GPGGA'):
        msg=pynmea2.parse(data)
        print(msg)
        time.sleep(2)