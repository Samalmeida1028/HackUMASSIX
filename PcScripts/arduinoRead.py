from typing import final
import serial
import time
import sys

import MorseCodeConverter as m

def initialize(arduino):
    refVal = 0
    averageNoise = 0
    while refVal < 10:
        temp = getVoltageValues(arduino)
        if temp != -1:
            averageNoise += temp[1]
            refVal += 1
    averageNoise /= refVal
    return averageNoise + 35

# initialize Arduino
def calibrate(inputType, arduino):
    threshold = initialize(arduino)
    intervals = []
    highLow = [0, 0]
    intervalStart = time.perf_counter()
    while True:
        newVoltage = getVoltageValues(arduino)
        if newVoltage == -1:
            continue
        else:
            voltage = newVoltage
            if voltage[inputType] > threshold:
                if highLow[inputType] == 0:
                    intervals.append(time.perf_counter() - intervalStart)
                    intervalStart = time.perf_counter()
                highLow[inputType] = 1
            else:
                if highLow[inputType] == 1:
                    intervals.append(time.perf_counter() - intervalStart)
                    intervalStart = time.perf_counter()
                    latestEdit = [time.perf_counter(), True]
                highLow[inputType] = 0
            if len(intervals) >= 8:
                break
    return calculateOddAverage(intervals)

def loop(inputType, ditVal, epsilon, arduino):
    intervals = []
    finalResult = ''                    # keeps track of if PS or PR is clicked
    highLow = [0, 0]                    # intervalStart keeps track of time between clicks
    intervalStart = time.perf_counter() # When was the interval last updated?
                                        # and should we update the result string since new interval value was inserted?
    latestEdit = [time.perf_counter(), False]
    
    threshold = initialize(arduino)
    
    while True:
        voltages = getVoltageValues(arduino)
        if voltages == -1:
            continue
        else:                           # check if analog read voltage of PS|PR >= threshold voltage
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
                    print(m.morseToText(finalResult))
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
            if interval > (14 * ditVal):
                return -1
            elif interval > (4 * ditVal):
                result += "   "
            elif interval > (2 * ditVal):
                result += " "
        else:
            if interval < ditVal + epsilon:
                result += "."
            else:
                result += "-"
        i += 1
    return result

def getVoltageValues(arduino):
    arduinoInput = arduino.readline()                # read from the serial line
    #print(arduinoInput)
    voltageStrings = arduinoInput.decode("utf-8").split("|")
    print(voltageStrings)
    try:
        num1 = float(voltageStrings[0])
        num2 = float(voltageStrings[1])
    except:
        return -1
    else:
        return (num1, num2)

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

def takeMachineInput(ditVal, arduino):
    return m.morseToText(loop(1, ditVal, ditVal * 0.3, arduino)[0])

if __name__ == '__main__':
   print(startArduinoInput())
