import time

def rain_setup(pin=17):
	GPIO.setup(pin, GPIO.IN)
 
def rain_mainloop(ADC:PCF8591, GPIO:GPIO, pin=17):
    rain_status = 1
    while True:
        print (ADC.read(0))
        rain_tmp = GPIO.input(pin)
        if rain_tmp != rain_status:
            if rain_tmp:
                print("Raining")   
            else:
                print("Not rain")
            rain_status = rain_tmp 
        time.sleep(0.2)  