import time
import sys
import tm1637

display=tm1637.TM1637(23,24,2)
display.Clear()
display.SetBrightnes(1)
while(True):
    #DEAF
    word_to_display=[13,14,10,15]
    display.Show(word_to_display)
    time.sleep(1)

    #FACE
    word_to_display=[15,10,12,14]
    display.Show(word_to_display)
    time.sleep(1)

    #CAFE
    word_to_display=[12,10,15,14]
    display.Show(word_to_display)
    time.sleep(1)

    #FADE
    word_to_display=[15,10,13,14]
    display.Show(word_to_display)
    time.sleep(1)

    #CADE
    word_to_display=[12,10,13,14]
    display.Show(word_to_display)
    time.sleep(1)
    
'''
for i in range(0,len(numbers)):
    for j in range(0,len(numbers)):
        for k in range(0,len(numbers)):
            for l in range(0,len(numbers)):
                current_num=[]
                display.Show(current_num)
                time.sleep(1)
                '''
            
    
