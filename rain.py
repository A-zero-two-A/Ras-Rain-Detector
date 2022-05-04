import time
import PCF8591 as ADC
def rain_mainloop(ADC_addr=0):
    rain_status = 1
    while True:
        cur = ADC.read(ADC_addr)
        if cur <= 100:
            print("Raining..")
        else:
            print("Not rain")
        time.sleep(1)  