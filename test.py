import rain
import thermistor
import PCF8591 as ADC
import RPi.GPIO as GPIO

PCF_addr = '0x48'

def init():
    ADC.setup(PCF_addr)

if __name__ == '__main__':
    init()
    # rain.rain_mainloop(PCF_addr)
    thermistor.thm_loop(PCF_addr)