import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1000)      # initialize Arduino
def getVoltageValues():
    arduinoInput = arduino.readline()                # read from the serial line
    #print(arduinoInput)
    voltageStrings = arduinoInput.decode("utf-8").split("|")
    #print(voltageStrings)
    return (float(voltageStrings[1]), float(voltageStrings[0]))

def initialize():
    refVal = 10
    averageNoise = 0
    for i in range(0, refVal):
        voltages = getVoltageValues()
        averageNoise += float(voltages[1])
    averageNoise /= refVal
    return averageNoise

intervals = ([], [])
ditVal = 0.5
dahVal = 1.5
epsilon = 0.1

def loop():
    # keeps track of time between clicks
    intervalStart = [0, 0]
    # keeps track of if PS or PR was clickled previously
    prevHighLow = [0, 0]
    # keeps track of if PS or PR is clicked currently
    highLow = [0, 0]
    
    thresholds = [0.00, initialize()]
    while True:
        voltages = getVoltageValues()

        # check if click changed for PS and PR
        #print(thresholds)
        for i in range(0, 2):
            # check if analog read voltage of PS|PR >= threshold voltage
            if voltages[i] > thresholds[i]:
                if highLow[i] == 0:
                    print("NICE1")
                    intervals[i].append(time.perf_counter() - intervalStart[i])
                    print(intervals[i][-1])
                highLow[i] = 1
            else:
                if highLow[i] == 1:
                    print("NICE2")
                    intervalStart[i] = time.perf_counter()
                highLow[i] = 0

        optimize()

def optimize():
    pass
    # temp
    #print(intervals)


if __name__ == '__main__':
    loop()