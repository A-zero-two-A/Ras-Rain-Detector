import time
import adafruit_dht


def init(pin):
    """
    Initial the dht device  初始化DHT11
    :param pin: pin the adafruit_dht_11 use
    :return: dhtDevice
    """
    return adafruit_dht.DHT11(pin)


def get_info(dhtDevice):
    while True:
        try:
            # 如成功获取温湿度, 直接返回
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
            return temperature_c, humidity
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            # 根据官方说明↑, 忽视这个错误并重试
            print(error.args[0])
            time.sleep(2)
            continue
        except Exception as error:
            # 检测到其他错误, raise至上一层
            dhtDevice.exit()
            raise error
