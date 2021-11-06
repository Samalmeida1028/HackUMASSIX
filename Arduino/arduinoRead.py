import serial
import time

arduino = serial.Serial(port='COM8', baudrate=9600, timeout=1000)      # initialize Arduino

def loop():
    while True:
        voltage = arduino.readline()                # read from the serial line
        strings = voltage.decode("utf-8").split(" ")
        vPD = strings[0]
        vPS = strings[1]

        pd = 0
        ps = 0
        if vPS >= "10.00":  # check if analog read voltage >= threshold voltage
            pd = "PD: 1"
        else:
            pd = "PD: 0"

        if vPD >= "50.00":
            ps = "PS: 1"
        else:
            ps = "PS: 0"
        print(pd, ps)

if __name__ == '__main__':
    loop()