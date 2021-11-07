import serial
import time
import sys

from MorseCodeConverter import morseToText

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1000)      # initialize Arduino

def getVoltageValues():
    arduinoInput = arduino.readline()                # read from the serial line
    #print(arduinoInput)
    voltageStrings = arduinoInput.decode("utf-8").split("|")
    #print(voltageStrings)
    return (float(voltageStrings[0]), float(voltageStrings[1]))

def initialize():
    refVal = 10
    averageNoise = 0
    for i in range(0, refVal):
        voltages = getVoltageValues()
        averageNoise += float(voltages[1])
    averageNoise /= refVal
    return averageNoise * 1.05

intervals = ([], [])

ditVal = 1
dahVal = 3
epsilon = 0.4

def loop(inputType):

    finalResult = ''

    #Flush buffer
    arduino.readline()
    time.sleep(0.01)

    # keeps track of if PS or PR is clicked
    highLow = [0, 0]
    # intervalStart keeps track of time between clicks
    intervalStart = time.perf_counter()
    # When was the interval last updated? 
    # and should we update the result string since new interval value was inserted?
    latestEdit = [time.perf_counter(), False]
    
    if inputType:
        threshold = initialize()
    else:
        threshold = 0.10

    while True:
        voltages = getVoltageValues()

        # check if analog read voltage of PS|PR >= threshold voltage
        if voltages[inputType] > threshold:
            if highLow[inputType] == 0:
                intervals[inputType].append(time.perf_counter() - intervalStart)
                intervalStart = time.perf_counter()
                latestEdit = [time.perf_counter(), True]
            highLow[inputType] = 1
        else:
            if highLow[inputType] == 1:
                intervals[inputType].append(time.perf_counter() - intervalStart)
                intervalStart = time.perf_counter()
                latestEdit = [time.perf_counter(), True]
            highLow[inputType] = 0

        if latestEdit[1]:
            result = intervalsToMorse(inputType)
            if result == -1:
                break
            else:
                finalResult = result
                latestEdit[1] = False
        elif (time.perf_counter() - latestEdit[0]) > (15 * ditVal):
            break
    return morseToText(finalResult)


def withinRange(toCheck, correctVal):
    return abs(toCheck - correctVal) < epsilon

def intervalsToMorse(inputType):
    result = ""
    i = 0
    for interval in intervals[inputType]:
        if i == 0:
            i += 1
            continue
        elif i % 2 == 0:
            if interval > (15 * ditVal):
                return -1
            elif interval > (6 * ditVal):
                result += "   "
            elif interval > (3 * ditVal):
                result += " "
        else:
            if interval < ditVal + epsilon:
                result += "."
            elif (ditVal + epsilon < interval) and (interval < dahVal + epsilon):
                result += "-"
            else:
                sys.exit()
        i += 1
    return result

if __name__ == '__main__':
    print(loop(1))