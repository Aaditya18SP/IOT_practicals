import time
import RPi.GPIO as GPIO
import telepot


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)


def handle(msg):
    chat_id=msg['chat']['id']
    command =msg['text']
    command =command.lower()
    print('Got command : %s'%command)
    
    if(command == "on" ):
        bot.sendMessage(chat_id,start_counter())
        return
    elif(command=="off"):
        bot.sendMessage(chat_id,stop_counter())
        return
def start_counter():    
    bina_hex= ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    '''bina_oct = ['000','001','010','011','100','101','110','111']'''
    '''bina_oct.len'''
    for i in range(0,len(bina_hex)):
        current=bina_hex[i]
        GPIO.output(11,int(current[0]))
        GPIO.output(13,int(current[1]))
        GPIO.output(15,int(current[2]))
        GPIO.output(12,int(current[3]))
        time.sleep(2)
    return
       
def stop_counter():
    return

bot=telepot.Bot('6339798154:AAF2tzyktbdbDAMXOhSsXZLk2pZ42KB7sFg')
bot.message_loop(handle)
print('I am listening...')     

    