import rain
import thermistor
import PCF8591 as ADC
import U_photo as up
import RPi.GPIO as GPIO

ADC_addr = {
    'rain': 0,
    'thm': 1
}

PCF_addr = 0x48

def init():
    ADC.setup(PCF_addr)

if __name__ == '__main__':
    init()
    # rain.rain_mainloop(ADC_addr['rain'])
    # thermistor.thm_loop(ADC_addr['thm'])
    # aDHT.DHT_mainloop()
    # ada.dht_mainloop()
    up.loop()