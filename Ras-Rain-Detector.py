import os
import time

import LED
import touch
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
ADC.setup(PCF_addr)
touch.init()

class RainDet(object):
    def __init__(self):
        self.is_rain = False
        self.tmp = 0.0
        self.win_closed = False
        self.warn = False
        self.cur_led_color = 0
        self.touch_num = 0
        up.init(self.up_callback)
        
    def init(self):
        self.query_data()
        self.change_led()
        self.show()
        
    def change_led(self):
        LED.change_LED(self.cur_led_color)
        if self.cur_led_color == 0:
            self.cur_led_color = 1
        else:
            self.cur_led_color = 0
        
    def warn_judge(self):
        if self.is_rain and self.win_closed != True:
            self.warn = True
        else:
            self.warn = False
    
    def up_callback(self, arg):
        if(GPIO.input(up.U_photo_PIPin)):
            self.win_closed = True
        else:
            self.win_closed = False
    
    def query_data(self):
        self.is_rain = rain.get_rain_info(ADC_addr['rain'])
        self.tmp = thermistor.get_thm(ADC_addr['thm'])
    
    def send_warn(self):
        self.change_led(self.cur_led_color)
        self.show()
        print('!!!Close the window!!!')
       
    def mainloop(self):
        while True:
            self.query_data()
            self.warn_judge()
            if self.warn:
                self.send_warn()
            if touch.is_touch(GPIO.input(36)):
                self.show()
            self.debug()
            time.sleep(1)

    def show(self):
        os.system('clear')
        print('Ras-Rain-Detector')
        print('Temp: '+str(self.tmp)+'C')
        print('Raining: '+str(self.is_rain))
        print('Window: ', end='')
        if self.win_closed:
            print('Closed')
        else:
            print('Opened')
            
    def debug(self):
        os.system('clear')
        print('Ras-Rain-Detector')
        print('Temp: '+str(self.tmp)+'C')
        print('Raining: '+str(self.is_rain))
        print('Window: ', end='')
        if self.win_closed:
            print('Closed')
        else:
            print('Opened')
        print(self.cur_led_color)
        print(self.warn)
        print(ADC.read(0))
        print(ADC.read(1))
        if touch.is_touch(GPIO.input(36)):
            self.touch_num += 1
        print("touch", end=str(self.touch_num))
        
    
    def release(self):
        GPIO.cleanup()
    
if __name__ == '__main__':
    rd = RainDet()
    rd.init()
    try:
        while True:
            rd.mainloop()
    except KeyboardInterrupt:
        rd.release()
    except Exception:
        pass