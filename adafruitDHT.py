"""
Adafruit Mod
"""
import time
import board
import PCF8591 as ADC
import adafruit_dht

sensor_arg = '11'
dhtDevice = adafruit_dht.DHT22(board.D18)

def DHT_mainloop(GPIO_pin):
    while True:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
        time.sleep(1)