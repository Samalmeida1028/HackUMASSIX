import serial
import TextToOutput as T
import arduinoRead as ar
import arduinoWrite as aw

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1000)

receive = True
firstReceive = True

# toSend = "ALEXANDER GRAHAM BELL"
ditval = 1.4

if receive:     # this computer is the receiver
    if firstReceive:
        ditVal = ar.calibrate(1, arduino)

    print("CHECKPOINT %.4f" % ditVal)
    print(ar.takeMachineInput(ditVal, arduino))

    calibration1 = ar.loop(1, 0.75, 0.3)
    ditVal = ar.calculateOddAverage(calibration1[1])

    print(ar.takeMachineInput(ditVal, arduino))
else:           # this computer is the sender
    string = input('Enter input string in English: ')
    l = T.textToOutput(string)  # get the string of sums to work with

    # for char in l:
    #     if char != '1':
    #         print(char, end = '')

    aw.writeToArduino(l, arduino)