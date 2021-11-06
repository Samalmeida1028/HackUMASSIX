import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1000)      # initialize Arduino

def loop():
    intervals = []
    prevPD = 0
    prevPS = 0
    while True:
        voltage = arduino.readline()                # read from the serial line
        strings = voltage.decode("utf-8").split("|")
        vPD = float(strings[0])
        vPS = float(strings[1])

        if vPS >= 10.00:  # check if analog read voltage >= threshold voltage
            PS = 1
        else:
            PS = 0

        if vPD >= 50.00:
            PD = 1
        else:
            PD = 0
        
        if prevPD == 0:
            if PD == 1:
                intervalStart = time.process_time()
        elif prevPD == 1:
            if PD == 0:
                intervals.append(time.process_time() - intervalStart)


if __name__ == '__main__':
    loop()