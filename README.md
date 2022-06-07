# Ras-Rain-Detector

肝度:[![wakatime](https://wakatime.com/badge/user/b2ca97db-bce2-4b9b-8588-23c0de16890a/project/4abdce95-6975-4e73-ac71-6ba798d263ca.svg)](https://wakatime.com/badge/user/b2ca97db-bce2-4b9b-8588-23c0de16890a/project/4abdce95-6975-4e73-ac71-6ba798d263ca)

USTB Raspberry Development homework

----

## Intro

`Ras-Rain-Detector`是一款可以实时监测天气并提醒用户及时关窗的程序, 基于树莓派平台实现

### 背景

下雨时, 家中窗户较多, 可能出现漏关的状况, 该程序可以在下雨时检测到未关闭的窗户并提醒用户, 待机时还可以显示当前的外温作为温度计使用

实际应用时, 在窗户相应部位安装遮光板和光电门, 连接好树莓派即可完成组建, 可以作为时下热门的智能家居的**原型**进一步迭代开发或升级技术手段

### 使用到的组件

- PCF8591模块
- 温度传感器
- 雨滴传感器
- U型光电传感器
- LED传感器
- 触摸传感器
- RaspberryPi 4b


### 系统功能介绍

#### 实时气温检测

启动程序后会在控制台显示`当前气温` `降水情况` `关窗情况`等, 待机指示灯绿色常量, 当用户**触摸按钮**查询时会更新控制台数据

````
Ras-Rain-Detector
Temp: 26.9C
Raining: False
Window: Opened
````

#### 下雨关窗提醒

当检测到下雨且用户窗户打开时, 会提醒用户关窗, 此时指示灯变为红色, 窗户关闭后重新变绿

```
Ras-Rain-Detector
Temp: 21.9C
Raining: True
Window: Opened
!!!Close the window!!!
```

---

> 以下是开发文档

##  端口规范

### PCM8591

`AIN0`雨滴

`AIN1`湿度

### 树莓派

#### LED

```
makerobo_R = 11 (17)
makerobo_G = 12 (18)
makerobo_B = 13 (27)
```

#### 触摸

```
makerobo_TouchPin = 16 (36)
```

#### U型光电

```
U_photo_PIPin  = 40
```

## API

### 触摸开关模块

`touch.py`

封装函数`is_touch`, 检测到触摸返回`True`, 否则返回`False`

### LED模块

`LED.py`

待机状态指示灯绿色常亮

函数`change_LED`, 被调用时改变当前指示灯颜色, 红变绿, 绿变红

函数`clear_LED`, 被调用时关闭LED灯并释放`GPIO`接口


### 模拟温度传感模块

`thermistor.py`

函数`get_thm`, 调用时获取当前温度

### 雨滴传感模块

`rain.py`

函数`get_rain_info`, 调用时返回当前是否下雨

### 光电门传感模块

`U_photo.py`

初始化函数`init`负责设置`GPIO`时间监听器

函数`loop`在输入变化时显示当前状态


