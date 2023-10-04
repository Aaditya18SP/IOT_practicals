import time
import RPi.GPIO as GPIO
import tm1637

display= tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL)
display.Clear()
display.SetBrightnes(1)

even=list()
odd=list()

def findAllEvenOddNumbers():
    for i in range(20):
        if(i%2==0):
            even.append(i)
        elif(i%2==1):
            odd.append(i)

    
            
def displayNumbers():
    findAllEvenOddNumbers()
    word =[14,14,14,14]
    display.Show(word)
    time.sleep(2)
    
    #loop through the even numbers
    for i in even:
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
        time.sleep(1)
     
     #display odd numbers
    word=[13,13,13,13]
    display.Show(word)
    time.sleep(2)
    
    #loop through the odd numbers
    for i in odd:
        num_str= str(i)
        
        zero_str=""
        if(len(num_str) < 4 ):
            zero_str=addLeadingZeros(num_str)
            
        zero_str+=num_str    
        num_to_display=[int(zero_str[0]),int(zero_str[1]),int(zero_str[2]),int(zero_str[3])]
        display.Show(num_to_display)
        time.sleep(1)
        
def addLeadingZeros(var):
    zeros_str=""
    zeros_to_add= len("0000") - len(var)
    for i in range (zeros_to_add):
        zeros_str += "0"
    return zeros_str

displayNumbers()