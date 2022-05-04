from ast import If
import RPi.GPIO as GPIO

makerobo_TouchPin = 11   # 触摸传感器管脚PIN

makerobo_tmp = 0    #是否有触摸判断 

# GPIO口定义
def makerobo_setup():
	GPIO.setmode(GPIO.BOARD)       # 采用实际的物理管脚给GPIO口
	GPIO.setwarnings(False)        # 忽略GPIO操作注意警告
	GPIO.setup(makerobo_TouchPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # 设置makerobo_TouchPin管脚为输入模式，上拉至高电平(3.3V)

# 打印函数，显示出是否有触摸
def is_touch(x):
	global makerobo_tmp
	if x != makerobo_tmp:
		if x == 1:
			return True
		if x == 0:
			return False
		makerobo_tmp = x