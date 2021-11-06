import serial
import time

arduino = serial.Serial(port='COM8', baudrate=9600, timeout=1000)      # initialize Arduino

def loop():
