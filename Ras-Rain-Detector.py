import os
import time

import ada
import LED
# import touch
import rain
import thermistor
import PCF8591 as ADC
import U_photo as up
import RPi.GPIO as GPIO
import sender
import board

# PCM8591变量地址, 使用字典建立映射, 增加代码可读性
ADC_addr = {
    'rain': 0,
    'thm': 1
}

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
ada_pin = board.D16

# 初始化PCM8591 AD模块
PCF_addr = 0x48
ADC.setup(PCF_addr)
# touch.init()


class RainDet(object):
    """
    Ras-Rain-Detector类
    """
    def __init__(self):
        """
        构造函数, 初始化参数
        """
        self.d_tmp = 0.0
        self.is_rain = False
        self.tmp = 0.0
        self.win_closed = False
        self.warn = False
        self.cur_led_color = 0
        self.hum = 0.0
        # self.touch_num = 0
        self.dht_device = ada.init(ada_pin)
        up.init(self.up_callback)

    def init(self):
        """
        初始化函数, 程序启动时执行
        """
        self.query_data()
        self.change_led()
        self.show()

    def change_led(self):
        """
        翻转LED颜色(绿和红), 常规为绿色, 报警为红色
        """
        LED.change_LED(self.cur_led_color)
        if self.cur_led_color == 0 and self.warn:
            self.cur_led_color = 1
        elif self.cur_led_color == 1 and not self.warn:
            self.cur_led_color = 0

    def warn_judge(self):
        """
        判断是否报警
        :return: 设置成员warn的值
        """
        if self.is_rain and self.win_closed != True:
            self.warn = True
        else:
            self.warn = False

    def up_callback(self, argu):
        """
        判断窗户是否打开
        :return: 设置成员win_closed的值
        """
        if (GPIO.input(up.U_photo_PIPin)):
            self.win_closed = True
        else:
            self.win_closed = False

    def query_data(self):
        """
        查询数据方法, 获取所有传感气的数据并赋值给成员
        """
        self.is_rain = rain.get_rain_info(ADC_addr['rain'])
        self.tmp = thermistor.get_thm(ADC_addr['thm'])
        self.d_tmp, self.hum = ada.get_info(self.dht_device)

    def send_warn(self):
        """
        发出警报, 改变LED颜色并打印提示信息
        """
        self.change_led()
        self.show()
        print('!!!Close the window!!!')

    def mainloop(self):
        """
        主循环
        """
        while True:
            self.query_data()
            self.warn_judge()
            self.change_led()
            if self.warn:
                self.send_warn()
            # if touch.is_touch(GPIO.input(36)):
            self.show()
            self.send()
            time.sleep(1)

    def send(self):
        """
        参数上云
        """
        if self.win_closed:
            win = 1
        else:
            win = 0
        if self.is_rain:
            is_rain = 1
        else:
            is_rain = 0
        msg_dict = {
            'tem': (self.d_tmp + self.tmp) / 2,
            'hum': self.hum,
            'win': win,
            'is_rain': is_rain
        }
        sender.send(msg_dict)


    def show(self):
        """
        信息打印函数
        """
        os.system('clear')  # 清屏, 优化显示
        print('Ras-Rain-Detector')
        print('Temp: ' + str((self.tmp + self.d_tmp)/2) + 'C')
        print('Humd: '+ str(self.hum) + '%')
        print('Raining: ' + str(self.is_rain))
        print('Window: ', end='')
        if self.win_closed:
            print('Closed')
        else:
            print('Opened')

    def debug(self):
        os.system('clear')
        print('Ras-Rain-Detector')
        print('Temp: ' + str(self.tmp) + 'C')
        print('Humd: '+ str(self.hum) + '%')
        print('Raining: ' + str(self.is_rain))
        print('Window: ', end='')
        if self.win_closed:
            print('Closed')
        else:
            print('Opened')
        print(self.cur_led_color)
        print(self.warn)
        print(ADC.read(0))
        print(ADC.read(1))
        # if touch.is_touch(GPIO.input(36)):
        #     self.touch_num += 1
        # print("touch", end=str(self.touch_num))


    def release(self):
        """
        释放GPIO资源
        """
        GPIO.cleanup()


if __name__ == '__main__':
    # 创建实例
    rd = RainDet()

    # 初始化
    rd.init()

    # 主循环
    try:
        while True:
            rd.mainloop()
    except KeyboardInterrupt:
        rd.release()
