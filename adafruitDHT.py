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
        try:
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            print(
                "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                    temperature_f, temperature_c, humidity
                )
            )
            time.sleep(1)
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error    
    