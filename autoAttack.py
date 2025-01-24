import uiautomator2 as u2
import numpy as np
from PIL import Image
import pytesseract
import cv2
import re
import random

import time
 
# 使用设备唯一标志码链接设备，其中9phqaetw是通过adb获取的设备标志码
d = u2.connect('127.0.0.1:16384')
d.screenshot().save("./imgs/screenshot.png")

def get_allxy(img_model_path,threshold = 0.02):
        #传入一个图片，获取图片在全屏截图的位置
        
        #d.screenshot().save("./imgs/screenshot.png")
        #载入截图
        img = cv2.imread("./imgs/screenshot.png")
        
        #载入匹配截图
        img_terminal = cv2.imread(img_model_path)
        
        #读取模板的宽和高
        height,width=img_terminal.shape[0:2]
        
        # 进行模板匹配
        result = cv2.matchTemplate(img,img_terminal,cv2.TM_SQDIFF_NORMED )
        print(cv2.minMaxLoc(result))
        
        #threshold = 0.1  # 设置一个阈值，根据匹配程度调整
        loc = np.where(result <= threshold)
        
        # 如果找到匹配的位置，则输出它们
        if loc[0].size > 0:
            matches = []
            for pt in zip(*loc[::-1]):
                
                matches.append(pt)
            return matches
        else:
            
            print("Template goups not found\n")
            start_x, start_y= (233, 827)
            end_x, end_y = (233, 35)   
            start_x = int(start_x)
            start_y = int(start_y)
            end_x = int(end_x)
            end_y = int(end_y)

            d.swipe(start_x, start_y, end_x, end_y, duration=1)
            d.long_click(end_x, end_y)
            
            refresh_and_capture_screenshot()
            
            return 0

def recognize_text(matches,save_text_path,lang='chi_sim'):
    #接收坐标并识别图片
    
    #d.screenshot().save("./imgs/screenshot.png")
    #载入截图
    img = Image.open("./imgs/screenshot.png")
    
    matches_inform=[]
    for match in matches:
        
        #print(match)
        left, upper, right, lower = match
        crop_img = img.crop((left, upper, right, lower))
        save_path='./temps/crop_img'+str(match)+'.png'#截屏保存方便debug
        crop_img.save(save_path)
        text = pytesseract.image_to_string(crop_img, lang='chi_sim')

        # 打印识别结果
        print("识别结果：", text)
        
        text1 = text.strip().split("\n")
        if len(text1) == 2:
            second_line = text1[1]
            #print(second_line)
            
            pattern = r'[，., ]\s*'
            
            second_line=second_line.replace('(', '').replace(')', '')
            
            result_list = re.split(pattern, second_line)
            if len(result_list)==2:
                #print(result_list)
                inform_text='text:'+text1[0].replace(' ', '')+'\n'+'x:'+result_list[0]+'\n'+'y:'+result_list[1]+'\n'
                matches_inform.append(inform_text)
                with open(save_text_path, 'a', encoding='utf-8') as file:
                    file.write(inform_text+'\n')
            else:
                print("无法识别坐标")
        else:
            print("文本行数不正确，无法处理")
        # 这里可以对文本进行处理
        # with open('./documents/mark_informs.txt', 'a', encoding='utf-8') as file:
        #     file.write(text+'\n')
    print(matches_inform)
    return matches_inform
            
def recognize_mark_text(img_model_path_1,img_model_path_2,save_text_path):
    #识别个人标记地点图片文字
    
    #载入匹配截图
    img_terminal_1 = cv2.imread(img_model_path_1)
    img_terminal_2 = cv2.imread(img_model_path_2)
    
    #读取模板的宽和高
    y1,x1=img_terminal_1.shape[0:2]
    y2,x2=img_terminal_2.shape[0:2]
    
    nothas_duplicates=True
    inform_recognize_text=[]
    while nothas_duplicates:
        matches=get_allxy(img_model_path_1,0.02)#得到匹配的坐标
        print("matches:" + str(matches))
        if matches != 0:
            new_matches=[]
            for match in matches:
                #计算出需要识别的区域
                
                new_match=(match[0]+x1,match[1]-(y2-y1)/2,match[0]+x1+x2,match[1]+y2-(y2-y1)/2)
                new_matches.append(new_match)
                
            inform_recognize_text = inform_recognize_text + recognize_text(new_matches,save_text_path)
            print(inform_recognize_text)
            original_list = inform_recognize_text
            
            unique_set = set(original_list)
            
            nothas_duplicates = len(original_list) == len(unique_set)#如果长度相等则表示没有重复元素

            if(nothas_duplicates):
                start_x, start_y= (233, 827)
                end_x, end_y = (233, 35)   
                start_x = int(start_x)
                start_y = int(start_y)
                end_x = int(end_x)
                end_y = int(end_y)

                d.swipe(start_x, start_y, end_x, end_y, duration=1)
                d.long_click(end_x, end_y)
                
                refresh_and_capture_screenshot()
            else:
                print("结束")
                break
            
        
        
        
        

def get_xy(img_model_path,threshold = 0.1):
    #传入一个图片，获取图片在全屏截图的位置
        
        #载入截图
        img = cv2.imread("./imgs/screenshot.png")
        
        #载入匹配截图
        img_terminal = cv2.imread(img_model_path)
        
        #读取模板的宽和高
        height,width=img_terminal.shape[0:2]
        
        # 进行模板匹配
        result = cv2.matchTemplate(img,img_terminal,cv2.TM_SQDIFF_NORMED )
        #print(cv2.minMaxLoc(result))
        
        #threshold = 0.1  # 设置一个阈值，根据匹配程度调整
        loc = np.where(result <= threshold)
        
        # 如果找到匹配的位置，则输出它们
        if loc[0].size > 0:
            
            #  解析匹配区左上角的坐标
            upper_left = cv2.minMaxLoc(result)[2]
        
            #计算匹配区域右下角的坐标
            lower_right = (upper_left[0] + width,upper_left[1] + height)
        
            #计算需要点击的坐标
            avg = (((upper_left[0]+ lower_right[0])/2),((upper_left[1]+ lower_right[1])/2))

            return avg
        else:
            print(f"Template not found:{img_model_path}\n")
            return (-1,-1)
    
    
    
def auto_click(var_avg,second):
    
    if var_avg[0] == -1 and var_avg[1] == -1:
        return 0
    
    else:
        #接收坐标并且点击
        d.long_click(var_avg[0],var_avg[1],second)
    
#封装auto_click，get_xy
def routine(img_model_path,name,second=0.1,threshold=0.1):
    avg=get_xy(img_model_path,threshold)
    print(f'正在点击{name}')
    
    if auto_click(avg,second) == 0:
        return False
    else:
        return True
    
#刷新全图截屏
def refresh_and_capture_screenshot(second=1):
    time.sleep(second)
    d.screenshot().save("./imgs/screenshot.png")
    
#验证图片是否出现
def isElementPresentInImage(img_model_path,threshold = 0.1):
    
    refresh_and_capture_screenshot(1)
    
    #载入截图
    img = cv2.imread("./imgs/screenshot.png")
        
    #载入匹配截图
    img_terminal = cv2.imread(img_model_path)
    
    # 进行模板匹配
    result = cv2.matchTemplate(img,img_terminal,cv2.TM_SQDIFF_NORMED )
    
    #threshold = 0.1  # 设置一个阈值，根据匹配程度调整
    loc = np.where(result <= threshold)
    
    # 如果找到匹配的位置，则输出true
    if loc[0].size > 0:
        return True
    else:
        return False

#routine("./imgs/up_map.png","放大地图")
def get_Alliance_marker_info(save_text_path):
    count=0
    while (count<1):
        if (isElementPresentInImage("./imgs/alliance_mark_1.png",0.02) or isElementPresentInImage("./imgs/alliance_mark_0.png",0.02)):
            
            count += 1
            
        else:
            routine("./imgs/up_map.png","放大地图",1,0.5)
            
            count = 0
            
        #print("count:"+str(count))
        
    count=0
    while(count<1):
        if isElementPresentInImage("./imgs/alliance_mark_1.png",0.01):
            count += 1
        
        elif routine("./imgs/alliance_mark_0.png","个人收藏地标"):
            count = 0
            
        else :
            break
        
    recognize_mark_text("./imgs/alliance_star.png","./imgs/mark_inform.png",save_text_path)

def get_personal_marker_info(save_text_path):
    count=0
    while (count<1):
        if (isElementPresentInImage("./imgs/personal_mark_1.png",0.01) or isElementPresentInImage("./imgs/personal_mark_0.png",0.01)):
            
            count += 1
            
        else:
            routine("./imgs/up_map.png","放大地图",1,0.5)
            
            count = 0
            
        #print("count:"+str(count))
        
    count=0
    while(count<1):
        if isElementPresentInImage("./imgs/personal_mark_1.png",0.01):
            count += 1
        
        elif routine("./imgs/personal_mark_0.png","个人收藏地标"):
            count = 0
            
        else :
            break
        
    recognize_mark_text("./imgs/personal_star.png","./imgs/mark_inform.png",save_text_path)

def troop_choose(text):
    if "1" in text[0]:
        d.long_click(0.076, 0.8,0.5)
        if not is_troop_full(200,841):
            print("队伍1未满员")
            return 0
    
    elif "2" in text[0]:
        d.long_click(0.196, 0.8,0.5)
        if not is_troop_full(408,841):
            print("队伍2未满员")
            return 0
            
        
    elif "3" in text[0]:
        d.long_click(0.338, 0.8,0.5)
        if not is_troop_full(617,841):
            print("队伍3未满员")
            return 0
            
    
    elif "4" in text[0]:
        d.long_click(0.466, 0.8,0.5)
        if not is_troop_full(825,841):
            print("队伍4未满员")
            return 0
            
    elif "5" in text[0]:
        d.long_click(0.606, 0.8,0.5)
        if not is_troop_full(1034,841):
            print("队伍5未满员")
            return 0
        
    else:
        print(f"无法识别部队命令: {text}")
        return 0

def respond_command(text,x,y):
    refresh_and_capture_screenshot(random.uniform(0.1, 1.0))
    
    #d.long_click(0.03,0.654,1)
    if routine("./imgs/up_map.png","放大地图",1,0.5):
        if isElementPresentInImage("./imgs/xy_location.png"):
            d.click	(0.766, 0.918)#点击输入
            xy_input= str(x)+'.' + str(y)
            d.clear_text()
            d.send_keys(xy_input)
            d.long_click(0.5,0.5,0.1)
            
            routine("./imgs/go_xylocation.png","前往")
            time.sleep(2)
            d.long_click(0.5,0.5,0.5)
            
            refresh_and_capture_screenshot(1)
            
            if "行军" in text:
                routine("./imgs/march.png","行军")
                if troop_choose(text)==0:
                    return 0
                    
            elif "攻占" in text:
                routine("./imgs/occupy.png","攻占")
                if troop_choose(text)==0:
                    return 0
                
            elif "驻守" in text:
                routine("./imgs/garrison.png","驻守")
                if troop_choose(text)==0:
                    return 0
                
            elif "攻城" in text:
                routine("./imgs/siege.png","攻城")
                if troop_choose(text)==0:
                    return 0
                
            else:
                print(f"无法识别行为命令: {text}")
                return 0
                
            refresh_and_capture_screenshot(1)
            is_battle=isElementPresentInImage("./imgs/mobilize.png") or isElementPresentInImage("./imgs/stopover.png") or isElementPresentInImage("./imgs/idle_troops.png")

            if is_battle:
                routine("./imgs/battle.png","出征")
            else :
                print("未能出征")
                return 0


def is_troop_full(x,y,limit=60):
    refresh_and_capture_screenshot()
    
    image_path = "./imgs/screenshot.png"
    image = Image.open(image_path)
    pixel = image.getpixel((x, y))
    print(f"Pixel at ({x}, {y}) has RGB value: {pixel}")
    if pixel[0]+pixel[1]+pixel[2] <= limit:
        #print(" no full")
        return False
    else :
        #print(" full")
        return True


                
def respond_file_data(file_path):
    
    parsed_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()  # 读取所有行到列表中
        i = 0
        while i < len(lines):
            # 检查当前行是否以'text:'开头
            if lines[i].startswith('text:'):
                # 提取text的值
                text = lines[i].split(':')[1].strip()
                # 读取下一行并提取x的值
                x = int(lines[i+1].split(':')[1].strip())
                # 读取再下一行并提取y的值
                y = int(lines[i+2].split(':')[1].strip())
                # 响应解析后的数据
                respond_command(text,x,y)
                print(f'text: {text}, x: {x}, y: {y}')
                # 如果需要，可以将它们添加到列表中
                parsed_data.append({'text': text,'x': x, 'y': y})
                # 移动到下一块数据的开始
                i += 3  # 跳过当前块的三行
            else:
                # 如果当前行不以'text:'开头，可能是文件格式有误或空行，我们简单地跳过它
                i += 1
           
    d.long_click(0.5,0.5,0.5)
    return parsed_data
                   
    
    
def main():
    i=0
    while 1:
        print(i)
        
        d.long_click(0.99,0.808,0.5)#	(0.368, 0.935)
        
        with open('./documents/mark_informs.txt', 'w', encoding='utf-8') as file:
            # 不需要写入任何内容，只需要打开并关闭文件即可
            print("mark_informs文件已被清空")
            pass
        
        with open('./documents/Alliance_coordinates.txt', 'w', encoding='utf-8') as file:
            # 不需要写入任何内容，只需要打开并关闭文件即可
            print("Alliance_coordinates文件已被清空")
            pass
        
        get_Alliance_marker_info("./documents/Alliance_coordinates.txt")#获取同盟坐标
        
        #get_personal_marker_info("./documents/mark_informs.txt")#获取个人坐标
        
        respond_file_data("./documents/Alliance_coordinates.txt")
        # respond_file_data("./documents/mark_informs.txt")
        # respond_file_data("./documents/mark_customize.txt")
        #respond_command("3行军",1294,188)

        
        i+=1
        
if __name__ == "__main__":
    main()
