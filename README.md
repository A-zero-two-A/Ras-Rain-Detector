# Ras-Rain-Detector

USTB Raspberry Development homework

##  端口规范

### PCM8591

`A0`雨滴

`A1`湿度

`A2`温度

### 树莓派

#### LED

#### 触摸

## 设计

### 触摸开关模块

`touch.py`

封装函数`is_touch`, 检测到触摸返回`True`, 否则返回`False`

### LED模块

`LED.py`

待机状态指示灯绿色常亮

封装函数`change_LED`, 被调用时改变当前指示灯颜色, 红变绿, 绿变红

封装函数`clear_LED`, 被调用时关闭LED灯并释放`GPIO`接口

### 温湿度传感模块

`adafruitDHT.py`

封装函数`start_read`连续读取当前温湿度并返回

> 代码参考 https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py

### 模拟温度传感模块

`thermistor.py`

封装函数`thm_loop`连续读取当前温度

### 雨滴传感模块

`rain.py`

封装函数`rain_mainloop`持续读取当前是否下雨
