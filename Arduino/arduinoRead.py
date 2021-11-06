import serial
import time

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
ditVal = 0.5
dahVal = 1.5
epsilon = 0.1

def loop():
    arduino.readline()
    time.sleep(0.01)

    # keeps track of time between clicks
    intervalStart = [0, 0]
    # keeps track of if PS or PR is clicked
    highLow = [0, 0]
    
    thresholds = [(0.10), initialize()]
    #print(thresholds)
    while True:
        voltages = getVoltageValues()
        #print(voltages)
        # check if click changed for PS and PR
        #print(thresholds)
        for i in range(0, 1):
            # check if analog read voltage of PS|PR >= threshold voltage
            if voltages[i] > thresholds[i]:
                if highLow[i] == 0:
                    #print("NICE1")
                    intervals[i].append(time.perf_counter() - intervalStart[i])
                    if i == 0:
                        print("PRESSURE")
                    elif i == 1:
                        print("Light")
                    print(intervals[i][-1])
                highLow[i] = 1
            else:
                if highLow[i] == 1:
                    #print("NICE2")
                    intervalStart[i] = time.perf_counter()
                highLow[i] = 0

        optimize()

def optimize():
    pass
    # temp
    #print(intervals)


if __name__ == '__main__':
    loop()