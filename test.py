# 引用uiautomator2包
import uiautomator2 as u2
 
# 使用设备唯一标志码链接设备，其中9phqaetw是通过adb获取的设备标志码
d = u2.connect('127.0.0.1:16384')  
# d = u2.connect()  # 当前只有一个设备时可以用这个

#检查并维持设备端守护进程处于运行状态
#d.healthcheck()

#打开调试开关
#d.debug = True
#d.info

 # 获取窗口大小
#print(d.window_size())
# 设备垂直输出示例: (1080, 1920)
# 设备水平输出示例: (1920, 1080)

# 获取当前应用程序信息。对于某些android设备，输出可以为空
#print(d.current_ime())

#获取设备序列号
#print(d.serial)

#获取WIFI IP
#print(d.wlan_ip)

#获取详细的设备信息
#print(d.device_info)

#d.unlock()  # 解锁屏幕
 
x,y = 50,50
#d.click(x,y)  # 点击屏幕坐标为 x,y 的点
#d.press("camera") # 相机

# 双击屏幕
##for i in range(1,100000):
##    d.double_click(x,y)
##    print(i)

# 长按
#d.long_click(x,y)
 
# 单机屏幕上字符为9的控件
#d(text="9").click()

# 单击屏幕
#d.click(x,y)  # x,y为点击坐标

# 双击屏幕
#d.double_click(x,y)
#d.double_click(x,y,0.1) # 默认两个单击之间间隔时间为0.1秒

# 长按
#d.long_click(x,y)
#d.long_click(x,y,0.5)  # 长按0.5秒（默认）

# 滑动
sx,sy=500,500
ex,ey=500,700
for i in range(1,1000):
    #d.swipe(sx, sy, ex, ey)
    d.swipe_ext('down')
    print(i)
    d.swipe_ext('up')
#d.swipe(sx, sy, ex, ey, 0.5) #滑动0.5s(default)

#拖动
##d.drag(sx, sy, ex, ey)
##d.drag(sx, sy, ex, ey, 0.5)#拖动0.5s(default)
# 滑动点 多用于九宫格解锁，提前获取到每个点的相对坐标（这里支持百分比）

# 从点(x0, y0)滑到点(x1, y1)再滑到点(x2, y2)
# 两点之间的滑动速度是0.2秒
#d.swipe((x0, y0), (x1, y1), (x2, y2), 0.2)
# 注意：单击，滑动，拖动操作支持百分比位置值。例：
#d.long_click(0.5, 0.5) #表示长按屏幕中心
