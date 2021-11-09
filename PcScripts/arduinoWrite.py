import serial
import TextToOutput as t
import time

'''Configure the arduino by sending 4 dit flashes between the computers. This will output a checkpoint
which should be about 1.25 seconds if everything is configured right given the delays are not changed.'''
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

        # data = arduino.readline().decode('utf-8')           # return value from arduino for debugging
        # print("SENT: {}".format(send))
        # print("RCVD: {}".format(data))

        time.sleep(delay * 0.25)

'''Takes the characters from the string and flashes the LED in MORSE. Each string is sent into the board
and the board flashes the LED. A readline() function is used to check if every char is sent properly.'''
def writeToArduino(string, arduino):
    count = 0
    instructionsTotal = len(string)                    # the string contains the entire set of instrs
    config(arduino)

    for i in string:
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
    arduino = serial.Serial(port='COM3', baudrate=115200, timeout=2)  # initialize arduino

    string = input('Enter input string in English: ')
    l = t.textToOutput(string)                              # get the string of sums to work with

    # for char in l:
    #     if char != '1':
    #         print(char, end = '')

    writeToArduino(l, arduino)