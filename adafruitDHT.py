"""
Adafruit Mod
"""
import time
import PCF8591 as ADC
import Adafruit_DHT

sensor_arg = '11'

def DHT_read(sensor=sensor_arg, pin=0):
    return Adafruit_DHT.read_retry(sensor, pin)

def DHT_mainloop(GPIO_pin):
    while True:
        print(DHT_read(sensor_arg, GPIO_pin))
        time.sleep(1)