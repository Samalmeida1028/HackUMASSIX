import serial
import time
import sys

import MorseCodeConverter as m

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

def loop(inputType, ditVal, epsilon):

    intervals = []

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
                intervals.append(time.perf_counter() - intervalStart)
                intervalStart = time.perf_counter()
                latestEdit = [time.perf_counter(), True]
            highLow[inputType] = 1
        else:
            if highLow[inputType] == 1:
                intervals.append(time.perf_counter() - intervalStart)
                intervalStart = time.perf_counter()
                latestEdit = [time.perf_counter(), True]
            highLow[inputType] = 0

        if latestEdit[1]:
            result = intervalsToMorse(intervals, ditVal, epsilon)
            if result == -1:
                break
            else:
                finalResult = result
                latestEdit[1] = False
        elif (time.perf_counter() - latestEdit[0]) > (15 * ditVal):
            break
    
    return (finalResult, intervals) 

def intervalsToMorse(intervals, ditVal, epsilon):
    result = ""
    i = 0
    for interval in intervals:
        if i == 0:
            i += 1
            continue
        elif i % 2 == 0:
            if interval > (15 * ditVal):
                return -1
            elif interval > (7 * ditVal):
                result += "   "
            elif interval > (3 * ditVal):
                result += " "
        else:
            if interval < ditVal + epsilon:
                result += "."
            elif (ditVal + epsilon < interval) and (interval < (ditVal * 3) + epsilon):
                result += "-"
            else:
                sys.exit()
        i += 1
    return result

#Calculates the average of all elements at odd indices of a list
def calculateOddAverage(intervals):
    print(intervals)
    sum = 0.0
    count = 0.0
    for i in range(1, len(intervals), 2):
        sum += intervals[i]
        count += 1
    return sum / count

def startArduinoInput():
    response = "NULL"
    inputType = 0
    while response != "Y" and response !="N":
        response = input("Are you using the pressure sensor instead of the light sensor? Y/N: ")
        if response == "Y":
            inputType = 0
        elif response == "N":
            inputType = 1
        else:
            print("Invalid argument")

    response = "NULL"
    while response != "Y":
        print("We will now begin calibration")
        print('Enter the letter "h" or four dits as input and wait 9 seconds: ')
        calibration1 = loop(inputType, 0.75, 0.3)
        ditVal = calculateOddAverage(calibration1[1])
        print("Your ditVal is %.2f and your dahVal is %.2f" % (ditVal, 3 * ditVal) )
        print("And you wait at least %.2f seconds to imply letter spacing and %.2f seconds for word spaces" % (ditVal * 3, 7 * ditVal))
        response = input("Is this value satisfactory? Y/N: ")
        if response == "Y":
            break
        elif response == "N":
            print("Restarting calibration")
        else:
            print("Invalid input")
    print("Now enter your message and wait %.2f seconds: " % (15 * ditVal))
    res = loop(inputType, ditVal, ditVal * 0.4)[0]
    print(res)
    return m.morseToText(res)

def takeMachineInput(ditval):
    return m.morseToText(loop(1, ditVal, ditVal * 0.4)[0])



if __name__ == '__main__':
    print(startArduinoInput())