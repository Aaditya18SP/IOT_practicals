import time
import sys
import tm1637

display=tm1637.TM1637(23,24,2)
display.Clear()
display.SetBrightnes(1)
#The logic used in Embedded system doesnt work here. In python,its simpler. All the work is done by the library
#numbers=[0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x67]
#numbers=[63,6,91,79,102,109,125,7,127,103]



for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,10):
                
                #current_num=[int(str(numbers[i]), 16),int(str(numbers[j]), 16),int(str(numbers[k]), 16),int(str(numbers[l]), 16)]
                #current_num=[numbers[i],numbers[j],numbers[k],numbers[l]]
                current_num=[i,j,k,l]
                display.Show(current_num)
                print(current_num)
                time.sleep(1)
                
            
    
