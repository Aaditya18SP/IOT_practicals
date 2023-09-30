import time
import sys
import telepot
import tm1637
import RPi.GPIO as GPIO

display=tm1637.TM1637(23,24,tm1637.BRIGHT_TYPICAL)
display.Clear()
display.SetBrightnes(10)

def handle(msg):
    chat_id=msg['chat']['id']
    command=msg['text']
    command=command.lower()
    print('Got command : %s'%command)
    if(command=='on'):
        bot.sendMessage(chat_id,display_systime())
        return
    elif(command=='off'):
        bot.sendMessage(stop_displaying())
        return
def display_systime():
    date=datetime.datetime.now()
    hour=date.hour
    minute=date.minute
    second=date.second
    time_disp=[int(hour/10),hour%10,int(minute/10),minute%10]
    
def stop_displaying():
    display.Clear()
    display.SetBrightnes(0)
    return

bot=telepot.Bot('6339798154:AAF2tzyktbdbDAMXOhSsXZLk2pZ42KB7sFg')
bot.message_loop(handle)
print('I am listening...')