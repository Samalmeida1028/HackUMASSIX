import TextToOutput as t
import serial
import time
from struct import *
arduino = serial.Serial(port='COM9', baudrate=115200, timeout=.1)
def write_read(x):
    print(x[1])
    arduino.write(x[1])
    data = ''
    data += arduino.readline().decode('utf-8')
    return data

string = input("Enter a string: ") # Taking input from user
l = t.textToOutput(string)
print(l)
for i in l:
    value = write_read(i)
print(value) # printing the value

