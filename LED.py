import RPi.GPIO as GPIO
import time

Rpin = 17
Gpin = 18

gh = GPIO.HIGH
gl = GPIO.LOW

# GPIO.setmode(GPIO.BOARD) #采用实际的物理管脚给GPIO口
GPIO.setwarnings(False) #去除GPIO口警告
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#循环函数
def change_LED(cur_color):
    if cur_color:
        GPIO.output(Gpin,gl)
        GPIO.output(Rpin,gh)
    else:
        GPIO.output(Rpin,gl)
        GPIO.output(Gpin,gh)

#资源释放     
def clear_LED():
    GPIO.cleanup()

if __name__ == '__main__':
    cur_color = 0
    change_LED(0)
    time.sleep(2)
    change_LED(1)
    time.sleep(2)
    clear_LED()
