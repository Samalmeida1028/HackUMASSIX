import TextToOutput as T
import arduinoRead as ar
import arduinoWrite as aw

receive = False
firstReceive = True

toSend = "ALEXANDER GRAHAM BELL"
if receive:
    if firstReceive:
        calibration1 = ar.loop(1, 0.75, 0.3)
        ditVal = ar.calculateOddAverage(calibration1[1])
    print(ar.testMachineInput(ditVal))
else:
    transformed = T.textToOutput(toSend)
    aw.writeToArduino(transformed)


