from PIL import Image
import pytesseract
import cv2
import re


image_path = "./temps/crop_img(240, 43.0, 451, 115.0).png"
# 打开图片
#image_path="crop_img(240, 265.5, 453, 334.5).png"
img = Image.open(image_path)

#img_terminal_2 = cv2.imread(image_path)

#print(img_terminal_2.shape[ :2])
# 进行文字识别
text = pytesseract.image_to_string(img,lang='chi_sim')
print("识别结果：", text)
text1 = text.strip().split("\n")
# 打印识别结果
print("处理结果：", text1)

if len(text1) > 1:
    second_line = text1[1]
    print(second_line)
    pattern = r'[，.,]\s*'
    
    second_line=second_line.replace('(', '').replace(')', '')
    
    result_list = re.split(pattern, second_line)
    print(result_list)
    
else:
    print("文本行数不足，无法处理第二行。")

