import rain
import PCF8591 as ADC
import RPi.GPIO as GPIO

PCF_addr = '8x40'

def init():
    adc = ADC()
    return adc

if __name__ == '__main__':
    adc = init()
    adc.setup(PCF_addr)
    rain.rain_mainloop(adc, PCF_addr)