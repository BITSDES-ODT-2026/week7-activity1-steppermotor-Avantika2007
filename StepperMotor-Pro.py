#to make it turn clockwise and anticlockwise manually
from machine import Pin
import time
l1=Pin(5, Pin.OUT)
l2=Pin(14, Pin.OUT)
l3=Pin(18, Pin.OUT)
l4=Pin(19, Pin.OUT)
while True:
    for i in range (500):
        l1.value(1)
        l2.value(0)
        l3.value(0)
        l4.value(0)
        time.sleep_ms(5)
        l1.value(0)
        l2.value(1)
        l3.value(0)
        l4.value(0)
        time.sleep_ms(5)
        l1.value(0)
        l2.value(0)
        l3.value(1)
        l4.value(0)
        time.sleep_ms(5)
        l1.value(0)
        l2.value(0)
        l3.value(0)
        l4.value(1)
        time.sleep_ms(5)
    for i in range (500):
        time.sleep_ms(5)
        l1.value(0)
        l2.value(0)
        l3.value(0)
        l4.value(1)
        time.sleep_ms(5)
        l1.value(0)
        l2.value(0)
        l3.value(1)
        l4.value(0)
        time.sleep_ms(5)
        l1.value(0)
        l2.value(1)
        l3.value(0)
        l4.value(0)
        time.sleep_ms(5)
        l1.value(1)
        l2.value(0)
        l3.value(0)
        l4.value(0)
        time.sleep_ms(5)
    
#--------------------------------------
#same thing but with lists
from machine import Pin
import time
l1=Pin(5, Pin.OUT)
l2=Pin(14, Pin.OUT)
l3=Pin(18, Pin.OUT)
l4=Pin(19, Pin.OUT)
l=[[1,0,0,0],[0,1,0,0], [0,0,1,0],[0,0,0,1]]
while True:
    for i in range (500):
        for i in l:
            l1.value(i[3])
            l2.value(i[2])
            l3.value(i[1])
            l4.value(i[0])
            time.sleep_ms(5)
    for i in range (500):
        for i in l:
            l1.value(i[0])
            l2.value(i[1])
            l3.value(i[2])
            l4.value(i[3])
            time.sleep_ms(5)
   
    

   
    
