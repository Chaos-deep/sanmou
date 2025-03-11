from PIL import Image

# 打开图像文件
image_path = './imgs/11.png'  # 替换为你的图像路径
image = Image.open(image_path)

# 获取图像的宽度和高度
width, height = image.size

x, y = 201,841
pixel = image.getpixel((x, y))
print(f"Pixel at ({x}, {y}) has RGB value: {pixel}")
if pixel[0]+pixel[1]+pixel[2] <= 50:
    print("1 no full")
else :
    print("1 full")


x, y = 409,841
pixel = image.getpixel((x, y))
print(f"Pixel at ({x}, {y}) has RGB value: {pixel}")
if pixel[0]+pixel[1]+pixel[2] <= 50:
    print("2 no full")
else :
    print("2 full")

x, y = 618,841
pixel = image.getpixel((x, y))
print(f"Pixel at ({x}, {y}) has RGB value: {pixel}")
if pixel[0]+pixel[1]+pixel[2] <= 50:
    print("3 no full")
else :
    print("3 full")

    
x, y = 826,841
pixel = image.getpixel((x, y))
print(f"Pixel at ({x}, {y}) has RGB value: {pixel}")
if pixel[0]+pixel[1]+pixel[2] <= 50:
    print("4 no full")
else :
    print("4 full")

x, y = 1035,841
pixel = image.getpixel((x, y))
print(f"Pixel at ({x}, {y}) has RGB value: {pixel}")
if pixel[0]+pixel[1]+pixel[2] <= 50:
    print("5 no full")
else :
    print("5 full")
#Pixel at (201, 841) has RGB value: (1, 0, 2)
#Pixel at (409, 841) has RGB value: (1, 0, 2)
#Pixel at (618, 841) has RGB value: (1, 0, 2)
#Pixel at (816, 841) has RGB value: (1, 0, 5)
#Pixel at (1035, 841) has RGB value: (0, 0, 2)

# 指定要提取RGB值的像素点坐标（例如，x=10, y=20）
#x, y = 10, 20

# # 确保坐标在图像范围内
# if 0 <= x < width and 0 <= y < height:
#     # 获取像素点的RGB值
#     for x in range(0,width):
#         y=841
#         pixel = image.getpixel((x, y))
#         print(f"Pixel at ({x}, {y}) has RGB value: {pixel}")
#         #Pixel at (201, 841) has RGB value: (1, 0, 2)
#         #Pixel at (410, 841) has RGB value: (1, 0, 2)
#         #Pixel at (618, 841) has RGB value: (1, 0, 2)
#         #Pixel at (826, 841) has RGB value: (1, 0, 5)
#         #Pixel at (1035, 841) has RGB value: (0, 0, 2)
        
# else:
#     print("Coordinates are out of image bounds.")