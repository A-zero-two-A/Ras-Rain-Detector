import time
import RPi.GPIO as GPIO

U_photo_PIPin  = 21  # U型光电传感器管脚定义

def init(callback_func):
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False) 
	GPIO.setup(U_photo_PIPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.add_event_detect(U_photo_PIPin, GPIO.BOTH, callback=callback_func, bouncetime=200)



# 打印函数，显示出是否有黑色物体挡住
def U_photo_Print(pin_in):
    if pin_in:	
        print('Blocked!') 
    else:
        print('Free!')
			

# 中断函数，检测到有物体挡住时，响应中断函数					
def U_photo_detect(arg):
	U_photo_Print(GPIO.input(U_photo_PIPin))   # 打印出检测到有物体挡住！
 


# 循环函数
def loop():
	while True:
		pass

def destroy():
	GPIO.cleanup()

# 程序入口
if __name__ == '__main__':
    try:
        init()
        loop()
    except KeyboardInterrupt:
        destroy()
