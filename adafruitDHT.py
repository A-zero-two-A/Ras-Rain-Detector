"""
Adafruit Mod
"""
import sys

import Adafruit_DHT

sensor_arg = '11'

def start_read(sensor=sensor_arg, pin=0):
    return Adafruit_DHT.read_retry(sensor, pin)