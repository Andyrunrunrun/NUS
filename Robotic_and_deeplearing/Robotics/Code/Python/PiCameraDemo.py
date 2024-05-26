# 导入所需的库
import signal
import sys
import cv2

# 从picamera2库中导入Picamera2、Preview、MappedArray
from picamera2 import Picamera2, Preview, MappedArray

# 导入时间库
import time

# 创建Picamera2实例
picam2 = Picamera2()

# 定义颜色和文字属性
green = (0, 255, 0)
red = (255, 0, 0)
font = cv2.FONT_HERSHEY_SIMPLEX
scale = 1
thickness = 2

# 定义一个应用时间戳的函数
def apply_timestamp(request):
    # 获取时间戳
    timestamp = time.strftime("%Y-%m-%d %X")
    # 将时间戳应用到图像上
    with MappedArray(request, "main") as m:
        cv2.putText(m.array, "SWS3009B Trial Lecture", (130, 470), font, scale, red, thickness)
        cv2.putText(m.array, timestamp, (0, 30), font, scale, green, thickness)

# 设置Picamera2的预览回调函数为apply_timestamp
picam2.pre_callback = apply_timestamp

# 创建相机配置
camera_config = picam2.create_preview_configuration()
# 配置相机
picam2.configure(camera_config)
# 开始预览
picam2.start_preview(Preview.QTGL)
# 启动相机
picam2.start()
# 等待20秒
time.sleep(20)
# 拍摄照片并保存为classPhoto.jpg
picam2.capture_file("classPhoto.jpg")