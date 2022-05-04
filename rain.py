import time
import PCF8591 as ADC
def rain_mainloop(ADC_addr=0):
    rain_status = 1
    while True:
        print (ADC.read(ADC_addr))
        # rain_tmp = GPIO.input(pin)
        # if rain_tmp != rain_status:
        #     if rain_tmp:
        #         print("Raining")   
        #     else:
        #         print("Not rain")
        #     rain_status = rain_tmp 
        time.sleep(1)  