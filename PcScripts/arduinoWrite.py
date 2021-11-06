import TextToOutput as t
import serial

arduino = serial.Serial(port='COM9', baudrate=9600, timeout=1000)



string = input('Put string: ')

l = t.textToOutput(string)

print(l)
