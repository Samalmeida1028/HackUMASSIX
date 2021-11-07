import serial
import TextToOutput as T
import arduinoRead as ar
import arduinoWrite as aw

receive = True
firstReceive = True

toSend = "ALEXANDER GRAHAM BELL"
ditval = 1.4
if receive:
    arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1000) 
    if firstReceive:
        ditVal = ar.calibrate(1, arduino)
    print("CHECKPOINT %.4f" % ditVal)
    print(ar.takeMachineInput(ditVal, arduino))
else:
    transformed = T.textToOutput(toSend)
    aw.writeToArduino(transformed)


