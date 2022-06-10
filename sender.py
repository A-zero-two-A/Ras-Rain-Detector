import aliLink, mqttd, rpi


# 三元素（iot后台获取）
ProductKey = 'h5fz0rTp7Xx'
DeviceName = 'raspberry-device'
DeviceSecret = "47e37e4e85f87e61cd2490fad3a235f4"
# topic (iot后台获取)
POST = '/sys/h5fz0rTp7Xx/raspberry-device/thing/event/property/post'  # 上报消息到云
POST_REPLY = '/sys/h5fz0rTp7Xx/raspberry-device/thing/event/property/post_reply'
SET = '/sys/h5fz0rTp7Xx/raspberry-device/thing/service/property/set'  # 订阅云端指令


# # 消息回调（云端下发消息的回调函数）
# def on_message(client, userdata, msg):
#     return


# # 连接回调（与阿里云建立链接后的回调函数）
# def on_connect(client, userdata, flags, rc):
#     pass

# 链接信息
Server, ClientId, userNmae, Password = aliLink.linkiot(DeviceName, ProductKey, DeviceSecret)

# mqtt链接
mqtt = mqttd.MQTT(Server, ClientId, userNmae, Password)
mqtt.subscribe(SET)  # 订阅服务器下发消息topic
mqtt.begin(on_message, on_connect)


# 信息获取上报，每10秒钟上报一次系统参数
def send(msg_dict):
    # 获取指示灯状态
    power_stats = int(rpi.getLed())
    if power_stats == 0:
        power_LED = 0
    else:
        power_LED = 1

    # CPU 信息
    CPU_temp = float(rpi.getCPUtemperature())  # 温度   ℃
    CPU_usage = float(rpi.getCPUuse())  # 占用率 %

    # RAM 信息
    RAM_stats = rpi.getRAMinfo()
    RAM_total = round(int(RAM_stats[0]) / 1000, 1)
    RAM_used = round(int(RAM_stats[1]) / 1000, 1)
    RAM_free = round(int(RAM_stats[2]) / 1000, 1)

    # Disk 信息
    DISK_stats = rpi.getDiskSpace()
    DISK_total = float(DISK_stats[0][:-1])
    DISK_used = float(DISK_stats[1][:-1])
    DISK_perc = float(DISK_stats[3][:-1])


    # 构建与云端模型一致的消息结构
    updateMsn = {
        'cpu_temperature': CPU_temp,
        'cpu_usage': CPU_usage,
        'RAM_total': RAM_total,
        'RAM_used': RAM_used,
        'RAM_free': RAM_free,
        'DISK_total': DISK_total,
        'DISK_used_space': DISK_used,
        'DISK_used_percentage': DISK_perc,
        'PowerLed': power_LED,
        'temperature': msg_dict['tem'],
        'humidity': msg_dict['hum'],
        'window': msg_dict['win'],
        'rain': msg_dict['is_rain']
    }
    JsonUpdataMsn = aliLink.Alink(updateMsn)
    print(JsonUpdataMsn)

    mqtt.push(POST, JsonUpdataMsn)  # 定时向阿里云IOT推送我们构建好的Alink协议数据