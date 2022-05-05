import math
import PCF8591 as ADC

def get_thm(adc_port:int):
    thm_analogVal = ADC.read(adc_port) # 读取AIN0上的模拟值
    thm_Vr = 5 * float(thm_analogVal) / 255 # 转换到5V范围
    thm_Rt = 10000 * thm_Vr / (5 - thm_Vr)
    thm_temp = 1/(((math.log(thm_Rt / 10000)) / 3950) + (1 / (273.15+25)))
    thm_temp = thm_temp - 263.15
    # print('temperature = ', thm_temp, 'C')
    return thm_temp
        