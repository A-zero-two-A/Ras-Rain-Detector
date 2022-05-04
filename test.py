import rain
import PCF8591 as ADC
import RPi.GPIO as GPIO

PCF_addr = '8x40'

def init():
    ADC.setup(PCF_addr)

if __name__ == '__main__':
    init()
    rain.rain_mainloop(PCF_addr)