import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1000)      # initialize Arduino

def loop():
    threshold = initialize()
    intervals = []
    prevPD = 0
    prevPS = 0
    while True:
        voltage = arduino.readline()                # read from the serial line
        strings = voltage.decode("utf-8").split(" ")
        vPD = float(strings[0])
        vPS = float(strings[1])

        if vPS >= 10.00:  # check if analog read voltage >= threshold voltage
            PS = 1
        else:
            PS = 0

        if vPD >= threshold:
            PD = 1
        else:
            PD = 0
        
        if prevPD == 0:
            if PD == 1:
                intervalStart = time.process_time()
        elif prevPD == 1:
            if PD == 0:
                intervals.append(time.process_time() - intervalStart)


def initialize():
    refVal = 10
    for i in range(0,refVal):
        voltage = arduino.readline()  # read from the serial line
        strings = voltage.decode("utf-8").split(" ")
        averageNoise += float(strings[1])
    averageNoise /= refVal
    return averageNoise


if __name__ == '__main__':
    loop()