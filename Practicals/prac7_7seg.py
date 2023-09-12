import tm1637
import sys
import time
import telepot
import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)
display=tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL)
display.Clear()
display.SetBrightnes(1)

def handle(msg):
    chat_id=msg['chat']['id']
    command=msg['text']
    
    command=command.lower()
    print("the command is:%s" % command)
    
    if(command == "on"):
        bot.sendMessage(chat_id,display_counter(1))
    elif(command =="off"):
        print("here")
        bot.sendMessage(chat_id,display_counter(0))
        
 
def display_counter(disp):
    
    
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                for l in range(0,10):
                    current_num=[i,j,k,l]
                    display.Show(current_num)
                    time.sleep(1)
                  
   
def stop_counter():
    display=tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL)
    
    
    display.Clear()
    display.SetBrightnes(0)
    return

bot=telepot.Bot('6507618998:AAHuTO-wa9p-cyqJe0ujCve9AZeFVsSqJO8')
bot.message_loop(handle)
print('I am listening...')