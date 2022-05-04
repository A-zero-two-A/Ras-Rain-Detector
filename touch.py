import RPi.GPIO as GPIO
import time

makerobo_TouchPin = 36   # 触摸传感器管脚PIN

makerobo_tmp = 0    #是否有触摸判断 


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
  
if __name__ == '__main__':
    while True:
        cur = is_touch(GPIO.input(makerobo_TouchPin))
        if cur:
            print('1')
        else:
            print('0')
        time.sleep(1)