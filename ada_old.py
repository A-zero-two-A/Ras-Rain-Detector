import Adafruit_DHT.common as ada

sensor = ada.DHT11

pin = 24

def dht_mainloop():
    while True:
        humidity, temperature = ada.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')