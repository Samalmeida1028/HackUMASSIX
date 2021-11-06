import serial
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1000)      # initialize Arduino

def loop():
    while True:
        voltage = arduino.readline()                # read from the serial line
        strings = voltage.decode("utf-8").split("|")
        vPD = float(strings[0])
        vPS = float(strings[1])

        if vPS >= 10.00:  # check if analog read voltage >= threshold voltage
            pd = 1
        else:
            pd = 0

        if vPD >= 50.00:
            ps = 1
        else:
            ps = 0
        print(pd, ps)

if __name__ == '__main__':
    loop()