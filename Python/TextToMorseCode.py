# path is CSV/file
import csv
#import numpy as np
import serial
import time

# file = open('CSV/input.csv', 'w+', newline='') -> create new file
# 'r' for reading 'w' for writing
# arr = file.readlines() creates an array of lines
# arr.split('|') -> splits by specified delimiter. make sure when you write data you separate values by delimiter
arduino = serial.Serial(port='COM8', baudrate=9600, timeout=.1)      # initialize Arduino

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

def test():
#put test cases in here
    while True:
        num = input("Enter a number: ") # Taking input from user
        value = write_read(num)
        print(value) # printing the value
        if num == "exit":
            break

if __name__ == '__main__':
    test()