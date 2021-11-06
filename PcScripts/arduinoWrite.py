import TextToOutput as t
import serial
import time
from struct import *
arduino = serial.Serial(port='COM9', baudrate=115200, timeout=.1)
def write_read(x):
    print(arduino.write(x[0]),
    arduino.write(x[1]))
    data = arduino.readline()
    return data

string = input("Enter a string: ") # Taking input from user
l = t.textToOutput(string)
print(l)
for i in l:
    value = write_read(i)
print(value) # printing the value

