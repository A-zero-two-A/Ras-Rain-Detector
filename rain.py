import PCF8591 as ADC

def get_rain_info(ADC_addr=0):
    cur = ADC.read(ADC_addr)
    if cur <= 150:
        return True
    else:
        return False
