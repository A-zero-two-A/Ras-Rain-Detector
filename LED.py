import RPi.GPIO as GPIO
import time

from touch import makerobo_setup

# colors = [0xFF0000, 0x00FF00, 0x0000FF, 0xFFFF00, 0xFF00FF, 0x00FFFF]
colors = [0xFF0000, 0x00FF00]
Rpin = 11
Gpin = 12
Bpin = 13
cur_color = 0
gh = GPIO.HIGH
gl = GPIO.LOW
GPIO.setmode (GPIO.BOARD) #采用实际的物理管脚给GPIO口
GPIO.setwarnings(False) #去除GPIO口警告
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

#初始化程序
# def makerobo_setup(Rpin=11 Gpin=12, Bpin=13):
# global pins
# global p_R, p_G, p_B
# pins ={'pin_R': Rpin, 'pin_G': Gpin, 'pin_B': Bpin}

# for i in pins:
#     GPIO.setup(pins[i],GPIO.OUT) #设置Pin模式为输出模式
#     GPIO.output(pins[i], GPIO.LOW) #设置Pin管脚为低电平(0V)关闭LED
# #由于RGB三色模块每一个LED达到一定的亮度，需要的电流值是不一样，所以设置的频率有区别
# P_R = GPIO.PWM(pins['pin_R'], 2000) #设置频率为2KHz
# p_G = GPIO.PWM(pins['pin G'], 1999)
# P_B = GPIO.PWM(pins['pin_B'], 5000)
# #初始化占空比为0(led关闭)
# p_R.start(0)
# p_G.start(0)
# p_B.start(0)

#按比例缩放函数
def makerobo_pwm_map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    

#关闭RGB-LED灯
def makerobo_off():
    GPIO.setmode (GPIO.BOARD) #采用实际的物理管脚给GPIO口
    for i in pins:
        GPIO.Setup(pins[i],GPIO.OUT) #设置Pin模式为输出模式
        GPIO.output(pins[i], GPIO.LOW) #设置Pin管脚为低电平(OV)关闭LED

#设置颜色
def makerobo_set_Color(col): #例如：co1 = 0x112233
    # R_val = (col & 0xff0000) >> 16
    # G_val = (col & 0x00ff00) >> 8
    # B_val = (col & 0x0000ff) >> 0
    # #把0-255的范围同比例缩小到0-100之间
    # R_val = makerobo_pwm_map(R_val, 0, 255, 0, 100)
    # G_val = makerobo_pwm_map(G_val, 0, 255, 0, 100)
    # B_val = makerobo_pwm_map(B_val, 0, 255, 0, 100)
    # p_R.ChangeDutvCvcle(100-R_val) #改变占空比
    # p_G.ChangeDutycycle(100-G_val) #改变占空比
    # p_B.ChangeDutyCycle(100-B_val) #改变占空比
    pass

#循环函数
def change_LED():
    # while True:
    #     for col in colors:
    #         makerobo_set_Color(col) #设置颜色
    #         time.sleep(2) #延时2s
    if cur_color:
        GPIO.output(Gpin,gl)
        GPIO.output(Rpin,gh)
    else:
        GPIO.output(Gpin,gl)
        GPIO.output(Gpin,gh)

#资源释放     
def clear_LED():
    # p_R.stop() #美闭红鱼PM
    # p_G.stop() #关闭绿色PWM
    # p_B.stop() #关闭蓝鱼PWM
    # makerobo_off() #关闭RGB-LED灯
    GPIO.cleanup() #释放资源

if __name__ == '__main__':
    time.sleep(2)
    change_LED()
    time.sleep(2)
    clear_LED()