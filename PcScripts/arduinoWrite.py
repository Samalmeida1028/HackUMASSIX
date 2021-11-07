import serial
from PcScripts import TextToOutput as t

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=1)

string = input("Enter a string: ")
l = t.textToOutput(string)
print(l)
i = 0
while i < len(l) - 2:
    send = str(l[i]) + str(l[i+1])
    arduino.write(bytes(send, 'utf-8'))
    i += 2
    data = arduino.readline().decode('utf-8')

    print('SENT: {}'.format(send))
    print('RCVD: {}'.format(data))