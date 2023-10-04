import time
import RPi.GPIO as GPIO
import tm1637

display= tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL)
display.Clear()
display.SetBrightnes(1)

even=list()
odd=list()

def findAllEvenOddNumbers():
    for i in range(1000):
        if(i%2==0):
            even.append(i)
        elif(i%2==1):
            odd.append(i)
            
def displayNumbers():
    findAllEvenOddNumbers()
    word =[14,14,14,14]
    tm1637.Show(word)
    time.sleep(5)
    for i in even:
        num_str= str(i)
        num_to_display=[int(num_str[0]),int(num_str[1]),int(num_str[2]),int(num_str[3])]
        tm1637.Show(num_to_display)
        time.sleep(1)
        
    word=[13,13,13,13]
    tm1637.Show(word)
    time.sleep(5)
    for i in odd:
        num_str= str(i)
        num_to_display=[int(num_str[0]),int(num_str[1]),int(num_str[2]),int(num_str[3])]
        tm1637.Show(num_to_display)
        time.sleep(1)

displayNumbers()