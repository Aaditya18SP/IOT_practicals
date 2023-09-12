import sys
import random
import time
import telepot
import RPi.GPIO as GPIO

def on(pin):
    GPIO.output(pin,GPIO.HIGH)
    return
def off(pin):
    GPIO.output(pin,GPIO.LOW)
    return 


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

def handle(msg):
    chat_id =msg['chat']['id']
    
    command = msg['text']
    
    #command= command.lower()

    print('Got command: %s' % command)

    if command == 'on':
       bot.sendMessage(chat_id, on(11))
    elif command =='off':
       bot.sendMessage(chat_id, off(11))

bot = telepot.Bot('6507618998:AAHuTO-wa9p-cyqJe0ujCve9AZeFVsSqJO8')
bot.getMe()
bot.message_loop(handle)
print('I am listening...')

    


