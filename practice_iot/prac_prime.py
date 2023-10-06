import time
import RPi.GPIO as GPIO
import tm1637

display=tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL)
display.Clear()
display.SetBrightnes(1)
prime_numbers=list()

def prime_numbers_chk():
    for i in range(2,1020):
        f=0
        for j in range (2,i):
            if(i%j==0):
                f=1
                break
        if(f==0):
            prime_numbers.append(i)


def displayNumbers():
    prime_numbers_chk()
    for i in prime_numbers:
        # convert the int to string  
        num_str= str(i)
        
        ##add leading zeros
        zero_str=""
        if(len(num_str) < 4 ):
            zero_str=addLeadingZeros(num_str)
        
        #append the num_str to leading zeros ie 000 + 2
        zero_str+=num_str
        
        #separate each digit from the string
        num_to_display=[int(zero_str[0]),int(zero_str[1]),int(zero_str[2]),int(zero_str[3])]
        display.Show(num_to_display)
        time.sleep(0.1)

def addLeadingZeros(var):
    zeros_str=""
    zeros_to_add= len("0000") - len(var)
    for i in range (zeros_to_add):
        zeros_str += "0"
    return zeros_str

displayNumbers()       