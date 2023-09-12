import sys
import time
import datetime
import RPi.GPIO as GPIO
import tm1637
'''CLK->GPIO23(Pin 16)
DIO->GOPIO24(PIN 18)'''
#display=tm1637.TM1637(23,24,tm1637,BRIGHT_TYPICAL)
display=tm1637.TM1637(23,24,7)
display.Clear()
display.SetBrightnes(1)
while(True):
    now=datetime.datetime.now()
    hour=now.hour
    minute=now.minute
    seconds=now.second
    print("hour:",hour ,"minutes:",minute,"seconds:",seconds)
    currenttime=[int(hour/10),hour%10,int(minute/10), minute%10]
    print(currenttime)
    display.Show(currenttime)
    display.ShowDoublepoint(seconds%2)
    time.sleep(1)
    