import TextToOutput as T
import arduinoRead as ar
import arduinoWrite as aw

receive = True
firstReceive = True

toSend = "HELP MEEEE"
if receive:
    if firstReceive:
        calibration1 = ar.loop(1, 0.75, 0.3)
        ditVal = ar.calculateOddAverage(calibration1[1])
    print(ar.testMachineInput(ditVal))
else:
    transformed = T.textToOutput(toSend)
    aw.writeToArduino(transformed)


