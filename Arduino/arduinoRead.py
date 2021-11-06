import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1000)      # initialize Arduino

def initialize():
    refVal = 10
    averageNoise = 0
    for i in range(0,refVal):
        voltage = arduino.readline()  # read from the serial line
        strings = voltage.decode("utf-8").split(" ")
        averageNoise += float(strings[1])
    averageNoise /= refVal
    return averageNoise

intervals = [[], []]
ditVal = 0.5
dahVal = 1.5
epsilon = 0.1

def loop():
    # 0 is for PS(PressureSensor), 1 is for PR (PhotoResistor)
    threshold = initialize()
    intervals = [[], []]
    # keeps track of time between clicks
    intervalStart = (0, 0)
    # keeps track of if PS or PR was clickled previously
    prevHighLow = (0, 0)
    # keeps track of if PS or PR is clicked currently
    highLow = (0, 0)
    while True:
        arduinoInput = arduino.readline()                # read from the serial line
        voltageStrings = arduinoInput.decode("utf-8").split(" ")
        voltages = (float(voltageStrings[0]), float(voltageStrings[1]))

        # check if analog read voltage of PS >= threshold voltage
        if voltages[0] > 10.00:
            highLow[0] = 1
        else:
            highLow[0] = 0

        # check if analog read voltage of PR >= threshold voltage
        if voltages[1] >= threshold:
            highLow[1] = 1
        else:
            highLow[1] = 0
        
        # check if click changed for PS and PR
        for i in range(0, 2):
            if prevHighLow[i] == 0:
                if highLow[i] == 1:
                    intervalStart[0] = time.process_time()
            elif prevHighLow[i] == 1:
                if highLow[i] == 0:
                    intervals[i].append(time.process_time() - intervalStart[i])
        optimize()

def optimize():
    # temp
    print(intervals)


if __name__ == '__main__':
    loop()