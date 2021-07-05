#!usr/bin/python3

from signal import signal, SIGTERM, SIGHUP, pause
# from smbus import SMBus
# from gpiozero import PWMLED

import signal
import smbus
import gpiozero

import inspect
import time

bus = smbus.SMBus(1)
led = gpiozero.PWMLED(26)
# the LED gets power from GPIO26:

def safe_exit(signum, frame):
    exit(1)


ads7830_commands = [0x84, 0xc4, 0x94, 0xd4, 0xa4, 0xe4, 0xb4, 0xf4]

def read_ads7830(inp): 
    bus.write_byte(0x4b, ads7830_commands[inp])      # 0x4b = 75
    return bus.read_byte(0x4b)


def values(inp):
    while True:
        value = read_ads7830(inp)
        print(value)
        led.value = value/255       # 255 is the largest number produced by the chip
        time.sleep(0.5)


signal.signal(signal.SIGTERM, safe_exit)
signal.signal(signal.SIGHUP, safe_exit)

try:
    values(0)
    signal.pause()

except KeyboardInterrupt:
    pass

finally:
    print("done")
    led.close()
