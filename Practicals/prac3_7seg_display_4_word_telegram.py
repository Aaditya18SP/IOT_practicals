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
        bot.sendMessage(chat_id,display_word())
        return
    elif(command=='off'):
        bot.sendMessage(stop_displaying())
        return

def display_word():
    word=[15,10,12,14]
    display.Show(word)
    time.sleep(2)
    word=[12,10,15,14]
    display.Show(word)
    time.sleep(2)
    word=[15,10,13,14]
    display.Show(word)
    time.sleep(2)
    word=[12,10,13,14]
    display.Show(word)
    time.sleep(2)
    return

def stop_displaying():
    display.Clear()
    display.SetBrightnes(0)
    return

bot=telepot.Bot('6339798154:AAF2tzyktbdbDAMXOhSsXZLk2pZ42KB7sFg')
bot.message_loop(handle)
print('I am listening...')