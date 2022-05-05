# Ras-Rain-Detector

[![wakatime](https://wakatime.com/badge/user/b2ca97db-bce2-4b9b-8588-23c0de16890a/project/4abdce95-6975-4e73-ac71-6ba798d263ca.svg)](https://wakatime.com/badge/user/b2ca97db-bce2-4b9b-8588-23c0de16890a/project/4abdce95-6975-4e73-ac71-6ba798d263ca)

USTB Raspberry Development homework

##  端口规范

### PCM8591

`A0`雨滴

`A1`湿度

`A2`温度

### 树莓派

#### LED

makerobo_R = 11 (17)
makerobo_G = 12 (18)
makerobo_B = 13 (27)

#### 触摸

makerobo_TouchPin = 16 (36)

#### U型光电

U_photo_PIPin  = 40

## 设计

### 触摸开关模块

`touch.py`

封装函数`is_touch`, 检测到触摸返回`True`, 否则返回`False`

### LED模块

`LED.py`

待机状态指示灯绿色常亮

封装函数`change_LED`, 被调用时改变当前指示灯颜色, 红变绿, 绿变红

封装函数`clear_LED`, 被调用时关闭LED灯并释放`GPIO`接口


### 模拟温度传感模块

`thermistor.py`

封装函数`thm_loop`连续读取当前温度

### 雨滴传感模块

`rain.py`

封装函数`rain_mainloop`持续读取当前是否下雨
