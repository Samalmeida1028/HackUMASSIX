import TextToOutput as t
import serial
import time
from struct import *
arduino = serial.Serial(port='COM9', baudrate=115200, timeout=.1)

string = input("Enter a string: ") # Taking input from user
l = list(t.textToOutput(string))
print(l)
for i in l:
    print(i)
    arduino.write(i)
    data = ''
    data += arduino.readline().decode('utf-8')
    print(data) # printing the value



