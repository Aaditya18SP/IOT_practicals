import time
import RPi.GPIO as GPIO
import telepot


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)#

GPIO.output(11,GPIO.LOW)
GPIO.output(12,GPIO.LOW)  
GPIO.output(13,GPIO.LOW)
GPIO.output(15,GPIO.LOW)

def handle(msg):
    chat_id=msg['chat']['id']
    command =msg['text']
    command =command.lower()
    print('Got command : %s'%command)
    
    if(command == "on" ):
        bot.sendMessage(chat_id,start_pattern())
        return
    elif(command=="off"):
        bot.sendMessage(chat_id,stop_pattern())
        return

def start_pattern():    
    while(1):
        GPIO.output(11,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(11,GPIO.LOW)
        time.sleep(1)
        GPIO.output(12,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(12,GPIO.LOW)
        time.sleep(1)
        GPIO.output(13,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(13,GPIO.LOW)
        time.sleep(1)
        GPIO.output(15,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(15,GPIO.LOW)
        time.sleep(1)
    return
def stop_pattern ():
    GPIO.output(11,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)  
    GPIO.output(13,GPIO.LOW)
    GPIO.output(15,GPIO.LOW)
    

#bot=telepot.Bot('6339798154:AAF2tzyktbdbDAMXOhSsXZLk2pZ42KB7sFg')
bot=telepot.Bot('5871889314:AAHyjtX3oFFMepdgbWycX8qNIdtEXgQ9YSM')
bot.message_loop(handle)
print('I am listening...')     