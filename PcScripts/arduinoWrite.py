import serial
import TextToOutput as t
import time

def config(arduino):
    time.sleep(1)
    l = '313131313166'
    for i in l:
        send = str(i)
        delay = .5
        if send == "2" or send == "3":                      # choose the delay value
            delay = 1
        elif send != "1":                                   # can only be 6 or 7 if not 2 or 3
            delay = 5

        arduino.write(bytes(send, 'utf-8'))
        data = arduino.readline().decode('utf-8')           # return value from arduino
        time.sleep(delay * 0.25)

def writeToArduino(string):
    arduino = serial.Serial(port='COM3', baudrate=115200, timeout=2)
    count = 0
    l = string
    instructionsTotal = len(l)
    config(arduino)
    for i in l:
        count+=1
        send = str(i)
        print(str(time.ctime())+ " sending %s of %s, %s%% of the way done" % (
            str(count), str(instructionsTotal), str((count / instructionsTotal) * 100)), end = '->')
        delay = .5

        if send == "2" or send == "3":                      # choose the delay value
            delay = 1
        elif send != "1":                                   # can only be 6 or 7 if not 2 or 3
            delay = 5
        arduino.write(bytes(send, 'utf-8'))
        data = arduino.readline().decode('utf-8')
        if send in data:
            print('success, %s received' %(send))
        else:
            print('failed')
        time.sleep(delay*.25)                               # Blink LED
        # LED kill sequence after code executes

if __name__ == '__main__':
    string = input('Enter input String: ')
    l = t.textToOutput(string)
    for char in l:
        if char != '1':
            print(char, end = '')
    writeToArduino(l)