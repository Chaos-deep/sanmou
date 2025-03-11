import uiautomator2 as u2

import numpy as np

import cv2

import time
 
# 使用设备唯一标志码链接设备，其中9phqaetw是通过adb获取的设备标志码
d = u2.connect('127.0.0.1:16384')
d.screenshot().save("./imgs/11.png")
print("finish")