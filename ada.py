import time
import adafruit_dht


def init(pin):
    """
    Initial the dht device
    :param pin: pin the adafruit_dht_11 use
    :return: dhtDevice
    """
    return adafruit_dht.DHT11(pin)


def get_info(dhtDevice):
    while True:
        try:
            # Print the values to the serial port
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            return temperature_c, humidity
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
