from time import sleep
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader=SimpleMFRC522()

try:
    text=input("Enter the data to write on a tag: ")
    print("Print your tag to write...")
    reader.write(text)
    print("Data written successfully")
finally:
    GPIO.cleanup()
