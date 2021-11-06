import serial
import time
import sys

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
    return (averageNoise, averageNoise * 0.05)

intervals = ([], [])

ditVal = 0.75
dahVal = 2.25
epsilon = 0.2

def loop():

    arduino.readline()
    time.sleep(0.01)

    # keeps track of time between clicks
    tempTime = time.perf_counter()
    intervalStart = [tempTime, tempTime]
    # keeps track of if PS or PR is clicked
    highLow = [0, 0]
    
    thresholds = [(0.10), initialize()]
    #print(thresholds)
    while True:
        voltages = getVoltageValues()

        # check if click changed for PS and PR
        for i in range(0, 1):
            # check if analog read voltage of PS|PR >= threshold voltage
            if voltages[i] > thresholds[i]:
                if highLow[i] == 0:
                    intervals[i].append(time.perf_counter() - intervalStart[i])
                    intervalStart[i] = time.perf_counter()
                highLow[i] = 1
            else:
                if highLow[i] == 1:
                    intervals[i].append(time.perf_counter() - intervalStart[i])
                    intervalStart[i] = time.perf_counter()
                highLow[i] = 0

        intervalsToMorse()
def withinDitRange(toCheck, correctVal):
    return abs(toCheck - correctVal) < epsilon

def intervalsToMorse():
    result = ""
    i = 0
    for interval in intervals[0]:
        if i == 0:
            continue
        elif i % 2 == 0:
            pass
        else:
            if withinRange(interval, dahVal):
                result += "-"
            elif withinDitRange(interval, ditVal):
                result += "."
            else:
                sys.exit()
        i += 1


if __name__ == '__main__':
    loop()