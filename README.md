# Ras-Rain_Detector

USTB Raspberry Development homework

##  接线

### PCM8591

`A0`雨滴

`A1`湿度

`A2`温度

## 设计

#### 触摸开关模块

`touch.py`

封装函数`is_touch`, 检测到触摸返回`True`, 否则返回`False`

#### LED模块

`LED.py`

待机状态指示灯绿色常亮

封装函数`change_LED`, 被调用时改变当前指示灯颜色, 红变绿, 绿变红

封装函数`clear_LED`, 被调用时关闭LED灯并释放`GPIO`接口



